#!/usr/bin/env python3
"""Varredura determinística de claims clínicos críticos nas cápsulas da P7.

Objetivo (Fase 9.1 da qualificação): produzir, sem julgamento de modelo, o
*denominador* da varredura clínica — quantas afirmações críticas existem, onde,
de que tipo, com que força de sinal, e quantas já estão rastreadas em
`registry/clinical_claims.jsonl`.

O que este script FAZ:
  - detecta lexicalmente candidatos a claim crítico por categoria e por FORÇA
    de sinal (`strong` = padrão específico e pouco ambíguo; `weak` = conectivo
    de prosa ou termo genérico, alto recall e baixa precisão);
  - classifica a seção da cápsula em que a linha aparece (`assertive_clinical`,
    `pedagogic_meta`, `historical`, `provenance`), porque um flashcard que diz
    uma dose é tão acionável quanto uma linha de conduta, enquanto um distrator
    afirma deliberadamente algo errado;
  - atribui um `detection_id` estável (hash do conteúdo normalizado);
  - liga detecções a claims registrados só com evidência textual explícita
    (tokens numéricos/unidades compartilhados), nunca por semelhança vaga;
  - emite cobertura por cápsula: detectado / registrado / não resolvido.

O que este script NÃO faz e não deve ser lido como fazendo:
  - não decide se um claim está clinicamente correto;
  - não decide vigência;
  - não fecha nenhum gate.
Detector lexical é o piso da varredura, não a adjudicação.

Denominador primário do gate `critical_claim_sweep`:
    tier == "strong" AND critical_category AND section_class == "assertive_clinical"
Os demais recortes ficam nos CSVs para auditoria e para medir a perda assumida.

Uso:
    python qualification/tools/critical_claim_scan.py --root p7-study-skill \
        --out qualification/reports
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import unicodedata
from pathlib import Path
from typing import Any, Iterable

SCHEMA_VERSION = "1.4.0"

# Changelog (v1.4.0): FINAL FREEZE. Achado da validacao fresca de recall
# pos-v1.3.0 (3a amostra, 12 capsulas, sem sobreposicao com as duas amostras
# anteriores — ver DETECTOR_VALIDATION_REPORT.md secao 11). Unico gap
# corrigido, por criterio explicito de "so reparar achado sistematico de alto
# risco, nao perseguir recall perfeito": verbos de CONTRAINDICACAO so
# casavam em forma participio/substantivo (contraindicado/contraindicacao),
# nao na forma verbal conjugada (contraindica/contraindicam) — igual ao
# problema ja corrigido para "evitar" em v1.2.0, mas que ficou faltando aqui.
# Achado real: "sangue no meato uretral | Contraindica sondagem cega" nao era
# capturado. Contraindicacao e uma das 5 categorias de dano prioritario.
#
# Gaps adicionais encontrados na mesma amostra e DELIBERADAMENTE NAO
# corrigidos (diminishing returns, nao sistematico/alto-risco o suficiente
# para justificar mais uma rodada): unidade "UFC/mL" ausente (corte de
# urocultura); "a partir de Xh" nao coberto (só anos/meses/semanas/dias);
# abreviacao "sem." faltando especificamente no padrao "ate Xsem."; forma
# adjetival "nao indicado" (vs. verbo "nao indicar") — este ultimo e
# direcao seguranca (sub-deteccao de uma NEGACAO e conservador, nao perigoso).
# Registrados como limitacao conhecida do detector congelado nesta versao.

# Changelog (v1.3.0): achado da REVALIDACAO de recall pos-v1.2.0 (amostra fresca,
# 18 capsulas sem sobreposicao com a amostra que motivou v1.2.0 — ver
# DETECTOR_VALIDATION_REPORT.md secao 7). Gap sistematico: intervalo de duracao
# "bare" (sem preposicao-gatilho), ex. "7-21 dias", "5-30 dias", "6-24 horas",
# "3 a 12 meses" — muito comum em tabelas de farmacocinetica e latencia
# diagnostica, incluindo timing de SNM/parkinsonismo farmacologico numa capsula
# de EMERGENCIA psiquiatrica de alto risco. Tambem: abreviacao "sem." (semanas)
# nao reconhecida pelos padroes existentes. Ambos corrigidos.

# Changelog (v1.2.0): correção pós-auditoria de recall (ver
# qualification/reports/DETECTOR_VALIDATION_REPORT.md). v1.1.0 (hash
# c8e340ce...) ficou congelado para a amostra de precisão/FN; os achados dessa
# amostra motivaram as mudanças abaixo, listadas explicitamente porque alteram
# o denominador e não podem ser silenciosas:
#   1) unidade cmH2O e taxa "/min" ausentes do vocabulário de dose;
#   2) "a partir de N anos", "por N dias/semanas/horas", "em N h" ausentes do
#      vocabulário de corte/janela;
#   3) verbos de contraindicação só casavam no infinitivo (evitar), não em
#      formas conjugadas (evitam, evita, evitando) nem em "nunca <verbo>";
#   4) sinônimo de emergência "rapidamente fatal" ausente;
#   5) `internacao_alta` promovida a categoria crítica — o prompt mestre §9.1
#      exige "internação/alta" entre os dez tipos de claim extraídos; a
#      exclusão anterior seguia uma leitura mais estreita de AGENTS.md e
#      escondia claims de dano real (ex.: critério obrigatório de internação
#      em transtorno alimentar grave);
#   6) MAIOR: o pacote usa quebra de linha rígida (~80 col) dentro de
#      parágrafos de prosa (conduta, conceito operacional mínimo, pivô
#      clínico). Um regex por linha física não vê "critérios de\ninternação"
#      como uma frase. A partir de v1.2.0, essas três seções também são
#      varridas em janelas de 2 linhas concatenadas, ancoradas na primeira
#      linha da janela, além da varredura linha-a-linha original.

# --------------------------------------------------------------------------
# Vocabulário
# --------------------------------------------------------------------------
# Unidades escritas por extenso ou com barra. Tokens de uma/duas letras que
# colidem com siglas clínicas (IC = insuficiência cardíaca, IO, U, L, G) ficam
# FORA do tier forte; foram causa comprovada de falso positivo na v1.0.0 do
# detector.
UNITS = (
    r"(?:mg/kg/dia|mcg/kg/min|mg/kg|mcg/kg|ml/kg|mg/dl|mg/l|g/dl|mmol/l|meq/l|"
    r"ng/ml|pg/ml|mg/m2|ui/kg|cmh2o|mg|mcg|µg|g|kg|ml|mmhg|mmol|meq|ui|%)"
)
RATE_UNITS = r"(?:ventilacoes|compressoes|respiracoes|batimentos)?\s*/\s*min\b"

ROUTES_EXPLICIT = (
    r"(?:via oral|endovenos[ao]|intravenos[ao]|intramuscular|subcutane[ao]|"
    r"intraosse[ao]|sublingual|inalatori[ao]|nebulizacao|retal|intranasal|"
    r"intratecal|topic[ao])"
)

# (padrao, tier). tier "strong" = especifico; "weak" = alto recall, baixa precisao.
CATEGORY_PATTERNS: dict[str, list[tuple[str, str]]] = {
    "dose_via_intervalo": [
        (rf"\b\d+(?:[.,]\d+)?\s*{UNITS}\b", "strong"),
        (rf"\b\d+(?:[.,]\d+)?\s*a\s*\d+(?:[.,]\d+)?\s*{UNITS}\b", "strong"),
        (r"\b1\s*:\s*\d{3,}\b", "strong"),
        (r"\b(?:dose|posologia|ataque|manutencao|bolus|diluicao|concentracao)\b.*\d", "strong"),
        (r"\b(?:dose maxima|maximo de|nao exceder|teto de)\b", "strong"),
        (r"\bcada\s+\d+\s*(?:h|horas|min|minutos|dias)\b", "strong"),
        (r"\bde\s*\d+\s*/\s*\d+\s*h\b", "strong"),
        (r"\b\d+\s*(?:x|vezes)\s*(?:ao |por )?dia\b", "strong"),
        (rf"\b{ROUTES_EXPLICIT}\b", "strong"),
        (rf"\b\d+(?:[.,]\d+)?\s*(?:-\s*\d+(?:[.,]\d+)?)?\s*{RATE_UNITS}", "strong"),
        (r"\b(?:ev|iv|im|vo|sc|sl)\b", "weak"),
        (r"\b(?:dose|posologia|infusao)\b", "weak"),
    ],
    "cutoff_escore_estadiamento": [
        (r"[<>≤≥]\s*\d", "strong"),
        (r"\b(?:cutoff|ponto de corte|limiar)\b", "strong"),
        (r"\b(?:escore|score|pontuacao)\b.*\d", "strong"),
        (r"\b(?:apgar|glasgow|child-pugh|curb-65|curb65|cha2ds2|nihss|hamilton|"
         r"panss|madrs|percentil|z-score|escala de)\b", "strong"),
        (r"\b(?:maior|menor) (?:que|do que)\s+\d", "strong"),
        (r"\b(?:acima|abaixo) de\s+\d", "strong"),
        (r"\ba partir de\s+\d+\s*(?:anos|meses|semanas|dias)\b", "strong"),
        (r"\b(?:estadiamento|estagio|classe funcional)\b", "strong"),
        (r"\b(?:classificacao|grau|classe)\b", "weak"),
        (r"\b(?:escore|score|pontuacao)\b", "weak"),
    ],
    "janela_temporal": [
        (r"\b(?:janela|dentro de|ate)\s+\d+(?:[.,]\d+)?\s*(?:h|horas|min|minutos|dias|semanas|meses)\b", "strong"),
        (r"\b(?:primeiras?|primeiros?)\s+\d+\s*(?:h|horas|min|minutos|dias|semanas|sem\.)\b", "strong"),
        (r"\b\d+\s*(?:h|horas|min|minutos)\s*(?:de|do|apos)\s*(?:inicio|ictus|sintoma|evento)\b", "strong"),
        (r"\b(?:minuto de ouro|golden hour|tempo porta|door-to-needle|door-to-balloon)\b", "strong"),
        (r"\b(?:aguda?|persistente|cronica?)\s*[<>≤≥]\s*\d", "strong"),
        (r"\bpor\s+\d+\s*(?:h|horas|min|minutos|dias|semanas|sem\.|meses)\b", "strong"),
        (r"\bem\s+\d+\s*(?:h|horas|min|minutos|dias|semanas|sem\.)\b", "strong"),
        (r"\d+\s*(?:[-–]|a)\s*\d+\s*(?:h|horas|min\.?|minutos|dias|semanas|sem\.|meses|anos)\b", "strong"),
        (r"\bjanela\b", "weak"),
    ],
    "contraindicacao_interacao": [
        (r"\b(?:contraindicad[oa]|contra-indicad[oa]|contraindicacao|contraindicacoes|"
         r"contraindic[ae]m?|contraindicando)\b", "strong"),
        (r"\bnao\s+(?:se\s+)?(?:usar|administrar|prescrever|associar|indicar|iniciar|realizar|fazer)\w*\b", "strong"),
        (r"\bnunca\s+(?:usar|administrar|prescrever|associar|indicar|iniciar|realizar|fazer)\w*\b", "strong"),
        (r"\b(?:interacao|interage com|potencializa|antagoniza)\b", "strong"),
        (r"\b(?:proscrit[oa]|vedado|jamais (?:usar|administrar))\b", "strong"),
        (r"\b(?:hipersensibilidade|alergia (?:previa|documentada))\b", "strong"),
        (r"\bevit(?:ar|a|am|ando|e|em)\b", "strong"),
        (r"\b(?:gestante|gravidez|lactacao|amamentacao)\b", "weak"),
    ],
    "emergencia_sinal_alarme": [
        (r"\b(?:sinal de alarme|sinais de alarme|sinal de alerta|sinais de alerta|red flag|"
         r"sinal de gravidade|sinais de gravidade)\b", "strong"),
        (r"\b(?:risco de (?:morte|obito)|potencialmente fatal|rapidamente fatal|ameaca a vida)\b", "strong"),
        (r"\b(?:parada cardiorrespiratoria|pcr|anafilaxia|estado de mal|status epilepticus|"
         r"cetoacidose|choque (?:septico|hipovolemico|cardiogenico|anafilatico)|sepse)\b", "strong"),
        (r"\b(?:risco (?:iminente|elevado) de suicid|ideacao suicida (?:estruturada|com plano)|"
         r"autoextermin|heteroagressividade)\b", "strong"),
        (r"\b(?:encaminhar imediatamente|conduta imediata|intervencao imediata|"
         r"transferir imediatamente)\b", "strong"),
        (r"\b(?:emergencia|urgencia)\b", "weak"),
        (r"\bimediatamente\b", "weak"),
    ],
    "sequencia_terapeutica": [
        (r"\b(?:primeira linha|segunda linha|terceira linha|1a linha|2a linha|3a linha)\b", "strong"),
        (r"\b(?:droga de escolha|tratamento de escolha|farmaco de escolha|conduta de escolha)\b", "strong"),
        (r"\b(?:somente apos|so apos|so entao|nunca antes de|antes de (?:iniciar|administrar|prescrever))\b", "strong"),
        (r"\b(?:refratari|falha terapeutica|nao respondeu a)\b", "strong"),
        (r"\b(?:escalonar|escalonamento|desmame|titulacao)\b", "strong"),
        (r"\b(?:etapa|passo)\s*\d\b", "strong"),
        (r"\b(?:antes de|apos|em seguida|na sequencia)\b", "weak"),
        (r"\b(?:iniciar com|comecar por|preferir)\b", "weak"),
    ],
    "internacao_alta": [
        (r"\b(?:criterio[s]? de (?:internacao|alta)|indicacao(?:es)? de internacao)\b", "strong"),
        (r"\binternacao\s+(?:e\s+)?obrigatori", "strong"),
        (r"\b(?:internar|internacao|hospitalizar|hospitalizacao)\b", "weak"),
        (r"\b(?:uti|cti|alta hospitalar|observacao por)\b", "weak"),
        (r"\b(?:referenciar|contrarreferencia|transferencia)\b", "weak"),
    ],
    "algoritmo_dependente_diretriz": [
        (r"\b(?:diretriz|guideline|protocolo|consenso)\b.*\b(?:19|20)\d{2}\b", "strong"),
        (r"\b(?:sbp|sbc|sbd|sbpt|abp|ministerio da saude|oms|who|aha|asa|esc|ada|nice|idsa|gina|gold)\b", "strong"),
        (r"\b(?:algoritmo|fluxograma|arvore de decisao)\b", "strong"),
        (r"\b(?:diretriz|guideline|protocolo|consenso|recomendacao)\b", "weak"),
        (r"\b(?:19|20)\d{2}\b", "weak"),
    ],
    "calendario_regra_jurisdicional": [
        (r"\b(?:calendario vacinal|esquema vacinal|dose de reforco|pni)\b", "strong"),
        (r"\b(?:notificacao compulsoria|portaria|resolucao cfm|rdc|lei n)\b", "strong"),
        (r"\b(?:anvisa|sus|cfm|caps|capsi|caps ad|raps)\b", "strong"),
        (r"\b(?:vacina|imunizacao)\b", "weak"),
        (r"\b(?:brasil|brasileir[oa]|rede publica)\b", "weak"),
    ],
    "afirmacao_absoluta": [
        (r"\bsempre\b", "strong"),
        (r"\bnunca\b", "strong"),
        (r"\bobrigatori[oa]\b", "strong"),
        (r"\bpadrao[- ]ouro\b", "strong"),
        (r"\bimperdoavel\b", "strong"),
        (r"\bexclusivamente\b", "strong"),
        (r"\btod[oa]s? (?:os|as) (?:pacientes|casos)\b", "strong"),
        (r"\bnenhum (?:paciente|caso)\b", "strong"),
        (r"\bzera\b", "strong"),
        (r"\bsuspens[oa]\b", "weak"),
    ],
}

COMPILED: dict[str, list[tuple[re.Pattern[str], str]]] = {
    name: [(re.compile(p), tier) for p, tier in pats] for name, pats in CATEGORY_PATTERNS.items()
}

# Categorias cuja detecção, em cápsula de alto risco, exige rastreabilidade
# (claim registrado ou quarentena explícita) antes de virar conduta assertiva.
# `afirmacao_absoluta`, `internacao_alta` e `algoritmo_dependente_diretriz` são
# sinalizadores de revisão, não claims críticos por si sós.
CRITICAL_CATEGORIES = {
    "dose_via_intervalo",
    "cutoff_escore_estadiamento",
    "janela_temporal",
    "contraindicacao_interacao",
    "emergencia_sinal_alarme",
    "sequencia_terapeutica",
    "calendario_regra_jurisdicional",
    "internacao_alta",
}

# Classificação de seção. Um flashcard que afirma uma dose é tão acionável
# quanto uma linha de conduta; um distrator afirma deliberadamente algo errado.
SECTION_CLASS: dict[str, str] = {
    "conceito operacional minimo": "assertive_clinical",
    "pivo clinico": "assertive_clinical",
    "palavras-ancora": "assertive_clinical",
    "dados de precisao": "assertive_clinical",
    "conduta": "assertive_clinical",
    "conduta e guardrails": "assertive_clinical",
    "cards minimos": "assertive_clinical",
    "revisao": "assertive_clinical",
    "a estacao": "assertive_clinical",
    "trombolise intravenosa": "assertive_clinical",
    "trombectomia mecanica": "assertive_clinical",
    "suporte que nao deve virar alvo automatico": "assertive_clinical",
    "operacao x movimento": "pedagogic_meta",
    "demanda x movimento": "pedagogic_meta",
    "como cai": "pedagogic_meta",
    "distratores sedutores": "pedagogic_meta",
    "pegadinhas": "pedagogic_meta",
    "pegadinhas e seguranca": "pedagogic_meta",
    "mini-casos ativos": "pedagogic_meta",
    "mini-casos ativos - responda antes de abrir": "pedagogic_meta",
    "mini-casos - responda antes de abrir": "pedagogic_meta",
    "metadados": "provenance",
    "fontes de vigencia clinica": "provenance",
    "estados de verificacao": "provenance",
    "camada de fonte": "provenance",
    "divergencias resolvidas": "provenance",
    "fontes ilegiveis / nao encontradas": "provenance",
    "pendencia a confirmar": "provenance",
    "reconciliacao das duas capsulas anunciadas": "provenance",
    "para a prova/material historico": "historical",
}


def strip_accents(text: str) -> str:
    return "".join(
        ch for ch in unicodedata.normalize("NFD", text) if unicodedata.category(ch) != "Mn"
    )


def normalize(text: str) -> str:
    return strip_accents(text).lower().replace("×", "x")


def classify_section(section_norm: str) -> str:
    if section_norm in SECTION_CLASS:
        return SECTION_CLASS[section_norm]
    if section_norm.startswith("pratica clinica atual"):
        return "assertive_clinical"
    if section_norm.startswith("mini-casos"):
        return "pedagogic_meta"
    if not section_norm:
        return "preamble"
    return "assertive_clinical"  # default seguro: tratar como acionável


def stable_id(*parts: str) -> str:
    return hashlib.sha256("␟".join(parts).encode("utf-8")).hexdigest()[:16]


NUM_TOKEN = re.compile(rf"\d+(?:[.,]\d+)?\s*{UNITS}|\d+(?:[.,]\d+)?")

# Locators de proveniencia (pagina/linha/versao) usam a MESMA forma "digito"
# que valores clinicos e viram falso positivo de ligacao se nao forem
# removidos ANTES de tokenizar. Achado real e verificado: "p.24" numa coluna
# de fonte da tabela "Dados de precisao" tokenizava para "24" e casava
# espuriamente com "24h" de um fato clinico completamente diferente (a
# DEFINICAO de diarreia linkando com uma dose de Plano C). Toda tabela de
# precisao do pacote tem coluna "Fonte (pagina)" — este nao e um caso raro.
CITATION_STRIP = re.compile(
    r"\b(?:pp?|pag(?:ina)?s?|l|linha|slide|quadro|tabela|figura|fig)\.?\s*"
    r"\d+(?:\s*[-–,]\s*\d+)*\b"
)
# Boilerplate de teto etário do calendario vacinal brasileiro (PNI), tipo
# "14a11m29d" — repete-se, com o MESMO valor final, em dezenas de vacinas
# distintas (convencao regulatoria "ate o dia anterior ao proximo
# aniversario"), entao NAO prova equivalencia entre duas vacinas diferentes.
AGE_CEILING_STRIP = re.compile(r"\b\d+a\d+m\d+d\b")

def _is_calendar_year(token: str) -> bool:
    return bool(re.fullmatch(r"(?:19|20)\d{2}", token))


def numeric_tokens(text: str) -> set[str]:
    cleaned = AGE_CEILING_STRIP.sub(" ", CITATION_STRIP.sub(" ", normalize(text)))
    out: set[str] = set()
    for match in NUM_TOKEN.finditer(cleaned):
        token = re.sub(r"\s+", "", match.group(0)).replace(",", ".")
        if token in {str(n) for n in range(0, 11)}:
            continue  # números de baixa informação (índices, contagens)
        if _is_calendar_year(token):
            # Achado real: "2026" (o ano corrente citado em quase toda
            # capsula/claim) satisfazia sozinho a regra de ">=2 numeros nus
            # em comum" ao se combinar com qualquer outro numero coincidente
            # — ano de diretriz nao e valor clinico, e citado universalmente.
            continue
        out.add(token)
    return out


# Seções de prosa corrida onde o markdown quebra linha em ~80 colunas dentro
# de uma mesma frase (ex.: "critérios de\ninternação"). `dados de precisao` e
# `cards minimos` são tabelas — cada linha física já é uma unidade completa —
# e não entram aqui.
PROSE_JOIN_SECTIONS = {
    "conceito operacional minimo", "pivo clinico", "conduta", "conduta e guardrails",
    "trombolise intravenosa", "trombectomia mecanica", "suporte que nao deve virar alvo automatico",
}


def _joinable_section(section: str) -> bool:
    return section in PROSE_JOIN_SECTIONS or section.startswith("pratica clinica atual")


def iter_capsule_lines(path: Path) -> Iterable[tuple[int, str, str]]:
    section = ""
    with path.open(encoding="utf-8") as handle:
        for line_no, raw in enumerate(handle, start=1):
            line = raw.rstrip("\n")
            heading = re.match(r"^#{1,6}\s+(.*)$", line)
            if heading:
                section = normalize(heading.group(1)).strip()
                continue
            if not line.strip():
                continue
            yield line_no, section, line


def iter_capsule_line_windows(path: Path) -> Iterable[tuple[int, str, str]]:
    """Janelas de 2 linhas consecutivas dentro da mesma seção de prosa,
    ancoradas na primeira linha, para capturar frase partida por quebra rígida
    de markdown. Linhas de tabela (`dados de precisao`, `cards minimos`) ficam
    de fora — cada linha de tabela já é uma unidade completa."""
    rows = list(iter_capsule_lines(path))
    for i in range(len(rows) - 1):
        line_no, section, text = rows[i]
        next_no, next_section, next_text = rows[i + 1]
        if not _joinable_section(section) or section != next_section:
            continue
        if next_no != line_no + 1:
            continue  # linhas em branco/tabela no meio quebram a janela
        if text.strip().startswith("|") or next_text.strip().startswith("|"):
            continue
        yield line_no, section, f"{text.rstrip()} {next_text.strip()}"


def detect(line: str) -> list[tuple[str, str]]:
    """Retorna [(categoria, tier)] com o tier mais forte por categoria."""
    norm = normalize(line)
    best: dict[str, str] = {}
    for category, patterns in COMPILED.items():
        for pattern, tier in patterns:
            if pattern.search(norm):
                if best.get(category) != "strong":
                    best[category] = tier
                if tier == "strong":
                    break
    return sorted(best.items())


def scan(root: Path) -> tuple[list[dict[str, Any]], dict[str, dict[str, Any]]]:
    catalog = json.loads((root / "artifacts" / "CAPSULE_CATALOG.json").read_text(encoding="utf-8"))
    capsules = {item["path"]: item for item in catalog["capsules"]}

    detections: list[dict[str, Any]] = []
    for rel_path in sorted(capsules):
        meta = capsules[rel_path]
        seen_at_line: set[tuple[int, str]] = set()  # (line_no, category) já reportado

        def add(line_no: int, section: str, text: str, source: str) -> None:
            hits = detect(text)
            if not hits:
                return
            section_class = classify_section(section)
            clean = text.strip()
            for category, tier in hits:
                key = (line_no, category)
                if key in seen_at_line:
                    continue
                seen_at_line.add(key)
                detections.append(
                    {
                        "detection_id": stable_id(rel_path, str(line_no), category, source, clean),
                        "capsule_id": meta["capsule_id"],
                        "capsule_path": rel_path,
                        "discipline": meta["discipline"] or "UNKNOWN",
                        "risk": meta["risk"] or "UNKNOWN",
                        "line_no": line_no,
                        "section": section,
                        "section_class": section_class,
                        "category": category,
                        "tier": tier,
                        "critical_category": category in CRITICAL_CATEGORIES,
                        "in_sweep_denominator": (
                            tier == "strong"
                            and category in CRITICAL_CATEGORIES
                            and section_class == "assertive_clinical"
                        ),
                        "source": source,
                        "text": clean,
                    }
                )

        for line_no, section, line in iter_capsule_lines(root / rel_path):
            add(line_no, section, line, "single_line")
        for line_no, section, joined in iter_capsule_line_windows(root / rel_path):
            add(line_no, section, joined, "joined_window")
    return detections, capsules


def load_registered(root: Path) -> list[dict[str, Any]]:
    records = []
    with (root / "registry" / "clinical_claims.jsonl").open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                records.append(json.loads(line))
    return records


def link(detections: list[dict[str, Any]], registered: list[dict[str, Any]]) -> None:
    """Liga detecção -> claim registrado apenas com evidência textual explícita.

    Critério (conservador de propósito): mesma cápsula E interseção não vazia de
    tokens numéricos/unidades. Sem token numérico em comum, a detecção permanece
    NÃO RESOLVIDA mesmo que o assunto pareça coberto. Coincidência temática não
    é rastreabilidade.
    """
    by_capsule: dict[str, list[dict[str, Any]]] = {}
    for record in registered:
        by_capsule.setdefault(record["capsule_id"], []).append(record)

    # ATENCAO: tokens vem SOMENTE de `statement` (a afirmacao clinica em si).
    # `curricular_context`, `notes` e `evidence` contem locators de pagina
    # ("p.24", "Quadro 6"), datas de revisao ("2026-08-20") e outros numeros de
    # proveniencia sem significado clinico. Incluir esses campos causou
    # ligacao espuria real e verificada: uma linha sobre "24h" na DEFINICAO de
    # diarreia linkava com um claim de Plano C só porque o claim citava "p.24"
    # como locator — coincidencia de numero de pagina, nao de conteudo clinico.
    # Ver qualification/reports/DETECTOR_VALIDATION_REPORT.md secao 9.
    claim_tokens = {
        record["claim_id"]: numeric_tokens(record.get("statement", ""))
        for record in registered
    }

    for det in detections:
        candidates = by_capsule.get(det["capsule_id"], [])
        det["capsule_has_registered_claims"] = bool(candidates)
        det_tokens = numeric_tokens(det["text"])
        linked = sorted(
            record["claim_id"]
            for record in candidates
            if is_material_match(det_tokens & claim_tokens[record["claim_id"]])
        )
        det["linked_claim_ids"] = " ".join(linked)
        det["link_basis"] = "shared_numeric_tokens" if linked else ""
        det["resolved"] = bool(linked)


def is_material_match(shared: set[str]) -> bool:
    """Um token numerico NU (sem unidade), tipo '14' ou '24', e comum demais
    para provar equivalencia material sozinho — achado real: '14' de 'aguda
    <=14 dias' casava por coincidencia com '14' de zinco 'por 10 a 14 dias',
    dois fatos clinicos diferentes.

    Mesmo com unidade, um token tipo '20mg' (inteiro redondo, unidade simples)
    ainda e comum o bastante para coincidir entre farmacos DIFERENTES — achado
    real: diazepam 'maximo total 20 mg' casava com fosfenitoina '20 mg PE/kg'
    numa capsula de status epilepticus, dois farmacos distintos, mesma dose
    redonda por coincidencia.

    Regra: exige >=1 token FORTE (contem '/', '.' ou '%' — unidade composta
    tipo mg/kg, decimal, ou percentual, muito menos propenso a coincidir), OU
    >=2 tokens numericos distintos em comum (coincidencia dupla e rara)."""
    if not shared:
        return False
    has_strong_token = any(re.search(r"[/.%]", token) for token in shared)
    return has_strong_token or len(shared) >= 2


def coverage(detections, capsules, registered) -> list[dict[str, Any]]:
    reg_by_capsule: dict[str, int] = {}
    for record in registered:
        reg_by_capsule[record["capsule_id"]] = reg_by_capsule.get(record["capsule_id"], 0) + 1

    by_path: dict[str, list[dict[str, Any]]] = {}
    for det in detections:
        by_path.setdefault(det["capsule_path"], []).append(det)

    rows = []
    for rel_path in sorted(capsules):
        meta = capsules[rel_path]
        mine = by_path.get(rel_path, [])
        denom = [d for d in mine if d["in_sweep_denominator"]]
        unresolved = [d for d in denom if not d["resolved"]]
        rows.append(
            {
                "capsule_id": meta["capsule_id"],
                "capsule_path": rel_path,
                "discipline": meta["discipline"] or "UNKNOWN",
                "risk": meta["risk"] or "UNKNOWN",
                "detections_total": len(mine),
                "sweep_denominator": len(denom),
                "sweep_denominator_lines": len({d["line_no"] for d in denom}),
                "claims_registered": reg_by_capsule.get(meta["capsule_id"], 0),
                "unresolved": len(unresolved),
                "coverage_pct": (
                    round(100.0 * (len(denom) - len(unresolved)) / len(denom), 2) if denom else 100.0
                ),
            }
        )
    return rows


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({key: row.get(key, "") for key in fieldnames})


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("p7-study-skill"))
    parser.add_argument("--out", type=Path, default=Path("qualification/reports"))
    args = parser.parse_args()
    root = args.root.resolve()
    out = args.out

    detections, capsules = scan(root)
    registered = load_registered(root)
    link(detections, registered)
    cov = coverage(detections, capsules, registered)

    write_csv(
        out / "CRITICAL_CLAIM_DETECTIONS.csv",
        detections,
        [
            "detection_id", "capsule_id", "capsule_path", "discipline", "risk", "line_no",
            "section", "section_class", "category", "tier", "critical_category",
            "in_sweep_denominator", "capsule_has_registered_claims", "linked_claim_ids",
            "link_basis", "resolved", "source", "text",
        ],
    )
    write_csv(
        out / "CRITICAL_CLAIM_COVERAGE.csv",
        cov,
        [
            "capsule_id", "capsule_path", "discipline", "risk", "detections_total",
            "sweep_denominator", "sweep_denominator_lines", "claims_registered",
            "unresolved", "coverage_pct",
        ],
    )

    denom = [d for d in detections if d["in_sweep_denominator"]]
    denom_high = [d for d in denom if d["risk"] == "high"]
    high_rows = [r for r in cov if r["risk"] == "high"]
    summary = {
        "schema_version": SCHEMA_VERSION,
        "capsules_scanned": len(capsules),
        "capsules_high_risk": len(high_rows),
        "claims_registered": len(registered),
        "detections_total": len(detections),
        "sweep_denominator": len(denom),
        "sweep_denominator_lines": len({(d["capsule_path"], d["line_no"]) for d in denom}),
        "sweep_denominator_high_risk": len(denom_high),
        "sweep_denominator_high_risk_lines": len(
            {(d["capsule_path"], d["line_no"]) for d in denom_high}
        ),
        "unresolved_total": sum(1 for d in denom if not d["resolved"]),
        "unresolved_high_risk": sum(1 for d in denom_high if not d["resolved"]),
        "capsules_high_risk_with_zero_registered_claims": sum(
            1 for r in high_rows if r["claims_registered"] == 0
        ),
        "excluded_from_denominator": {
            "weak_tier": sum(1 for d in detections if d["tier"] == "weak"),
            "non_critical_category": sum(1 for d in detections if not d["critical_category"]),
            "pedagogic_meta_section": sum(
                1 for d in detections if d["section_class"] == "pedagogic_meta"
            ),
            "provenance_section": sum(
                1 for d in detections if d["section_class"] == "provenance"
            ),
            "historical_section": sum(
                1 for d in detections if d["section_class"] == "historical"
            ),
        },
        "denominator_by_category": {
            category: sum(1 for d in denom if d["category"] == category)
            for category in sorted(CRITICAL_CATEGORIES)
        },
        "denominator_by_discipline": {
            discipline: sum(1 for d in denom if d["discipline"] == discipline)
            for discipline in sorted({d["discipline"] for d in denom})
        },
        "limitations": [
            "Detecção lexical: mede presença de afirmação crítica, não correção clínica.",
            "Tier `strong` reduz falso positivo mas não o elimina; tier `weak` fica fora do "
            "denominador e permanece no CSV — é perda de cobertura assumida, não zero.",
            "Ligação detecção->claim exige tokens numéricos compartilhados; coincidência "
            "temática sem número permanece não resolvida por decisão de segurança.",
            "Seções `pedagogic_meta` (distratores, pegadinhas, mini-casos, como cai) ficam fora "
            "do denominador porque afirmam o erro, não a conduta; permanecem auditáveis no CSV.",
            "Nenhum gate é fechado por este artefato.",
        ],
    }
    (out / "CRITICAL_CLAIM_SCAN_SUMMARY.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="",
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
