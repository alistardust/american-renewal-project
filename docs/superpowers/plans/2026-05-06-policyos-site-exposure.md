# PolicyOS Site Exposure Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Generate `docs/policyos.html` and per-pillar overlay sections from `policy/catalog/policy_catalog_v2.sqlite`, wiring PolicyOS into the live site.

**Architecture:** A one-time migration script (`scripts/migrate-policyos-to-db.py`) parses the three locked PolicyOS markdown sources and the inheritance matrix CSV into four new DB tables. A generation script (`scripts/generate-policyos.py`) reads the DB and writes `docs/policyos.html` and fills the sentinel regions in `docs/assets/js/data.js`. `app.js` reads those sentinels at runtime to inject the per-pillar overlay section. No hand-editing of generated output after initial run.

**Tech Stack:** Python 3.10+, `sqlite3` (stdlib), `markdown2` (PyPI), `re`, `csv`

**Spec:** `docs/superpowers/specs/2026-05-04-policyos-site-exposure-design.md` — read before implementing any chunk.

---

## File structure

### Created
| File | Purpose |
|---|---|
| `scripts/migrate-policyos-to-db.py` | One-time: parse markdown + CSV into 4 new DB tables, init data.js sentinels |
| `scripts/generate-policyos.py` | Idempotent generator: DB → `docs/policyos.html` + data.js sentinel fill |
| `scripts/requirements.txt` | Python deps: `markdown2` |
| `docs/policyos.html` | Generated output — do not hand-edit |

### Modified
| File | Change |
|---|---|
| `policy/catalog/policy_catalog_v2.sqlite` | 4 new tables: `policyos_layers`, `policyos_families`, `policyos_rules`, `policyos_pillar_overlays` |
| `docs/assets/js/data.js` | Two sentinel comment blocks appended after `window.siteData = siteData;` |
| `docs/assets/js/app.js` | PolicyOS nav item in hamburger tree; per-pillar `#pil-policyos` injection |
| `docs/classification.html` | Two "Under review" badges → "Locked"; remove stale paragraph; add link to policyos.html |
| `tests/unit/data.test.js` | 3 new describe blocks: policyosFamilies shape, overlays shape, KERN invariant |
| `tests/e2e/site.spec.js` | policyos.html describe block; per-pillar overlay test; classification badge test |
| `README.md` | Scripts table: 2 new rows |

---

## Chunk 1: DB migration + sentinel init

### Task 1: Create `scripts/requirements.txt`

**Files:**
- Create: `scripts/requirements.txt`

- [ ] **Step 1: Create file**

```
markdown2==2.5.3
```

- [ ] **Step 2: Verify install works**

```bash
pip install -r scripts/requirements.txt
```

Expected: installs without error.

---

### Task 2: Create `scripts/migrate-policyos-to-db.py`

**Files:**
- Create: `scripts/migrate-policyos-to-db.py`

This script is idempotent (uses `CREATE TABLE IF NOT EXISTS`, `INSERT OR REPLACE`). Run with `python3 scripts/migrate-policyos-to-db.py` from repo root.

- [ ] **Step 1: Write the migration script**

```python
#!/usr/bin/env python3
"""migrate-policyos-to-db.py

Populates four PolicyOS tables in policy_catalog_v2.sqlite from the three
locked markdown sources and the inheritance matrix CSV. Idempotent.

Run from repo root:
  python3 scripts/migrate-policyos-to-db.py

Then run the generation script:
  python3 scripts/generate-policyos.py
"""
import csv
import re
import sqlite3
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DB_PATH     = REPO / "policy/catalog/policy_catalog_v2.sqlite"
DATA_JS     = REPO / "docs/assets/js/data.js"
RULES_MD    = REPO / "policy/policyos/policyos_1_0_rules_proposal.md"
AUTHORING_MD = REPO / "policy/policyos/policyos_authoring_os_v1.md"
VALUES_MD   = REPO / "policy/policyos/policyos_platform_values_v1.md"
MATRIX_CSV  = REPO / "policy/policyos/policyos_1_0_inheritance_matrix.csv"

# ── Static canonical metadata (locked) ─────────────────────────────

LAYERS = [
    ("values",     "Platform Values",    "The moral and political anchor for all rules.",                              1),
    ("principles", "System Principles",  "Cross-platform design rules governing how policy must work.",               2),
    ("authoring",  "Authoring OS",       "How policy must be written, tested, scoped, enforced, and maintained.",     3),
]

# (code, layer_id, label, anchor_id, summary, sort_order)
FAMILIES = [
    ("KERN", "principles", "Core Kernel",                    "plos-kern", "Universal rules that apply to every pillar.",                                                              1),
    ("GEOG", "principles", "Geography & Access",             "plos-geog", "Rights and services may not vary by geography in ways that create unequal classes of people.",            2),
    ("FEDR", "principles", "Federalism & Anti-Centralization","plos-fedr","Power must be distributed to prevent single-point failure and abuse.",                                    3),
    ("REGD", "principles", "Regulatory Design",              "plos-regd", "Regulation must protect the public interest and resist capture by the regulated.",                        4),
    ("ENFA", "principles", "Enforcement Architecture",       "plos-enfa", "Enforcement must be designed, not assumed; penalties must be proportionate and actionable.",             5),
    ("AIGV", "principles", "AI Governance",                  "plos-aigv", "AI and algorithmic systems require transparency, accountability, and human oversight.",                  6),
    ("ECOL", "principles", "Ecological Habitability",        "plos-ecol", "Policy must not degrade the ecological conditions for human survival and flourishing.",                  7),
    ("THRV", "principles", "Material Security",              "plos-thrv", "Policy must actively secure the material preconditions for a dignified life.",                           8),
    ("DEMO", "principles", "Democratic Participation",       "plos-demo", "Policy must protect and expand the practical capacity for civic participation.",                         9),
    ("PRIV", "principles", "Privacy & Surveillance",         "plos-priv", "Policy must protect persons against surveillance, data exploitation, and coercive monitoring.",         10),
    ("ECON", "principles", "Economic Domination",            "plos-econ", "Policy must prevent and correct dangerous concentrations of private economic power.",                   11),
    ("NORM", "authoring",  "Normative Alignment",            "paos-norm", "Rules must be grounded in and aligned with the platform's core values.",                               12),
    ("AUTH", "authoring",  "Rule Construction",              "paos-auth", "Rules must be structurally complete, precise, and enforceable.",                                        13),
    ("TEST", "authoring",  "Validation & Adversarial Review","paos-test", "Rules must be reviewed for gaps, loopholes, edge cases, and abuse paths before adoption.",             14),
    ("ENFC", "authoring",  "Enforcement Design",             "paos-enfc", "Rules must specify enforcement actors, triggers, escalation, and remedies.",                           15),
    ("PLAC", "authoring",  "Scope & Placement",              "paos-plac", "Rules must be placed at the correct scope level — not too broad, not too narrow.",                     16),
    ("MAINT","authoring",  "Maintenance & Revision",         "paos-maint","Rules must have review cadences and mechanisms for revision, deprecation, and replacement.",           17),
]

# ── DB setup ────────────────────────────────────────────────────────

DDL = """
CREATE TABLE IF NOT EXISTS policyos_layers (
    id         TEXT PRIMARY KEY,
    label      TEXT NOT NULL,
    summary    TEXT NOT NULL,
    sort_order INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS policyos_families (
    code       TEXT PRIMARY KEY,
    layer_id   TEXT NOT NULL REFERENCES policyos_layers(id),
    label      TEXT NOT NULL,
    anchor_id  TEXT NOT NULL,
    summary    TEXT NOT NULL,
    sort_order INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS policyos_rules (
    id           TEXT PRIMARY KEY,
    family_code  TEXT REFERENCES policyos_families(code),
    layer_id     TEXT REFERENCES policyos_layers(id),
    sort_order   INTEGER NOT NULL,
    rule_text    TEXT NOT NULL,
    value_name   TEXT,
    rule_subtype TEXT
);

CREATE TABLE IF NOT EXISTS policyos_pillar_overlays (
    pillar_slug  TEXT NOT NULL,
    family_code  TEXT NOT NULL REFERENCES policyos_families(code),
    overlay_type TEXT NOT NULL,
    PRIMARY KEY (pillar_slug, family_code)
);
"""

# ── Parsing ─────────────────────────────────────────────────────────

def parse_system_principles(path: Path) -> list[tuple]:
    """Parse PLOS-*-NNNN rules from policyos_1_0_rules_proposal.md.

    Returns list of (id, family_code, layer_id, sort_order, rule_text).
    """
    text = path.read_text(encoding="utf-8")
    # Split into family blocks by h3 headings that contain backtick family codes
    family_block_re = re.compile(r'^### `([A-Z]+)`', re.MULTILINE)
    positions = [(m.start(), m.group(1)) for m in family_block_re.finditer(text)]
    rows: list[tuple] = []
    rule_re = re.compile(
        r'^\d+\.\s+`(PLOS-[A-Z]+-\d{4})`\n(.*?)(?=^\d+\.\s+`PLOS-|^###|\Z)',
        re.MULTILINE | re.DOTALL
    )
    for i, (start, family_code) in enumerate(positions):
        end = positions[i + 1][0] if i + 1 < len(positions) else len(text)
        block = text[start:end]
        for m in rule_re.finditer(block):
            rule_id   = m.group(1)
            rule_text = m.group(2).strip()
            sort_order = int(rule_id.split("-")[-1])
            rows.append((rule_id, family_code, "principles", sort_order, rule_text))
    return rows


def parse_authoring_os(path: Path) -> list[tuple]:
    """Parse PAOS-*-NNNN rules from policyos_authoring_os_v1.md.

    Returns list of (id, family_code, layer_id, sort_order, rule_text).
    """
    text = path.read_text(encoding="utf-8")
    # Rules are bullet-point single-line format: "- `PAOS-NORM-0001` text"
    rule_re = re.compile(r'^- `(PAOS-([A-Z]+)-(\d{4}))` (.+)$', re.MULTILINE)
    rows: list[tuple] = []
    for m in rule_re.finditer(text):
        rule_id    = m.group(1)
        family_code = m.group(2)
        sort_order = int(m.group(3))
        rule_text  = m.group(4).strip()
        rows.append((rule_id, family_code, "authoring", sort_order, rule_text))
    return rows


def parse_platform_values(path: Path) -> list[tuple]:
    """Parse floor/duty pairs from policyos_platform_values_v1.md.

    Returns list of (id, None, layer_id, sort_order, rule_text, value_name, rule_subtype).
    """
    text = path.read_text(encoding="utf-8")
    section_re = re.compile(
        r'^### (\d+)\. (.+?)\n(.*?)(?=^### \d+\.|\Z)',
        re.MULTILINE | re.DOTALL
    )
    floor_re = re.compile(r'Policy-writing floor:\n(.*?)(?=\n\nPolicy-writing duty:)', re.DOTALL)
    duty_re  = re.compile(r'Policy-writing duty:\n(.*?)(?=\n\n|\Z)', re.DOTALL)
    rows: list[tuple] = []
    for m in section_re.finditer(text):
        n          = int(m.group(1))
        value_name = m.group(2).strip()
        body       = m.group(3)
        floor_m    = floor_re.search(body)
        duty_m     = duty_re.search(body)
        if floor_m:
            rows.append((
                f"VAL-{n:04d}-FLOOR", None, "values",
                n * 10 - 1, floor_m.group(1).strip(),
                value_name, "floor"
            ))
        if duty_m:
            rows.append((
                f"VAL-{n:04d}-DUTY", None, "values",
                n * 10, duty_m.group(1).strip(),
                value_name, "duty"
            ))
    return rows


def parse_pillar_overlays(path: Path) -> list[tuple]:
    """Parse pillar_slug, family_code, overlay_type rows from CSV.

    Returns list of (pillar_slug, family_code, overlay_type).
    """
    rows: list[tuple] = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            slug = row["pillar_slug"].strip()
            for fam in row["mandatory_families"].split("|"):
                fam = fam.strip()
                if fam:
                    rows.append((slug, fam, "mandatory"))
            for fam in row["conditional_families"].split("|"):
                fam = fam.strip()
                if fam:
                    rows.append((slug, fam, "conditional"))
    return rows


# ── Sentinel init ────────────────────────────────────────────────────

SENTINEL_BLOCK = """
// %%POLICYOS-FAMILIES-BEGIN%%
siteData.policyosFamilies = [];
// %%POLICYOS-FAMILIES-END%%
// %%POLICYOS-OVERLAYS-BEGIN%%
siteData.policyosOverlays = {};
// %%POLICYOS-OVERLAYS-END%%
"""

def init_sentinels(data_js: Path) -> None:
    """Append sentinel comment blocks to data.js if not already present."""
    src = data_js.read_text(encoding="utf-8")
    if "%%POLICYOS-FAMILIES-BEGIN%%" in src:
        print("Sentinels already present in data.js — skipping.")
        return
    anchor = "window.siteData = siteData;"
    if anchor not in src:
        print(f"ERROR: anchor '{anchor}' not found in {data_js}", file=sys.stderr)
        sys.exit(1)
    updated = src.replace(anchor, anchor + SENTINEL_BLOCK, 1)
    data_js.write_text(updated, encoding="utf-8")
    print(f"Sentinel blocks appended to {data_js}.")


# ── Main ─────────────────────────────────────────────────────────────

def main() -> None:
    con = sqlite3.connect(DB_PATH)
    con.execute("PRAGMA foreign_keys = ON")
    cur = con.cursor()

    cur.executescript(DDL)

    # Layers
    cur.executemany(
        "INSERT OR REPLACE INTO policyos_layers VALUES (?,?,?,?)",
        LAYERS
    )

    # Families
    cur.executemany(
        "INSERT OR REPLACE INTO policyos_families VALUES (?,?,?,?,?,?)",
        FAMILIES
    )

    # System Principles rules
    sp_rows = parse_system_principles(RULES_MD)
    cur.executemany(
        "INSERT OR REPLACE INTO policyos_rules(id,family_code,layer_id,sort_order,rule_text) VALUES (?,?,?,?,?)",
        sp_rows
    )
    print(f"System Principles: {len(sp_rows)} rules inserted.")

    # Authoring OS rules
    ao_rows = parse_authoring_os(AUTHORING_MD)
    cur.executemany(
        "INSERT OR REPLACE INTO policyos_rules(id,family_code,layer_id,sort_order,rule_text) VALUES (?,?,?,?,?)",
        ao_rows
    )
    print(f"Authoring OS: {len(ao_rows)} rules inserted.")

    # Platform Values
    pv_rows = parse_platform_values(VALUES_MD)
    cur.executemany(
        "INSERT OR REPLACE INTO policyos_rules(id,family_code,layer_id,sort_order,rule_text,value_name,rule_subtype) VALUES (?,?,?,?,?,?,?)",
        pv_rows
    )
    print(f"Platform Values: {len(pv_rows)} floor/duty rows inserted.")

    # Pillar overlays — validate family codes at application layer
    valid_codes = {r[0] for r in cur.execute("SELECT code FROM policyos_families").fetchall()}
    overlay_rows = parse_pillar_overlays(MATRIX_CSV)
    bad = [(s, f) for s, f, _ in overlay_rows if f not in valid_codes]
    if bad:
        print(f"ERROR: unknown family codes in overlay CSV: {bad}", file=sys.stderr)
        con.rollback()
        sys.exit(1)
    cur.executemany(
        "INSERT OR REPLACE INTO policyos_pillar_overlays VALUES (?,?,?)",
        overlay_rows
    )
    print(f"Pillar overlays: {len(overlay_rows)} rows inserted.")

    con.commit()
    con.close()
    print("DB migration complete.")

    # Sentinel init in data.js
    init_sentinels(DATA_JS)


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Run the migration**

```bash
cd /home/alice/git/freedom-and-dignity-project
python3 scripts/migrate-policyos-to-db.py
```

Expected output (counts may vary slightly):
```
System Principles: 93 rules inserted.
Authoring OS: 43 rules inserted.
Platform Values: 22 floor/duty rows inserted.
Pillar overlays: ~50 rows inserted.
DB migration complete.
Sentinel blocks appended to docs/assets/js/data.js.
```

- [ ] **Step 3: Verify DB tables**

```bash
sqlite3 policy/catalog/policy_catalog_v2.sqlite \
  "SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'policyos%';"
```

Expected:
```
policyos_families
policyos_layers
policyos_pillar_overlays
policyos_rules
```

- [ ] **Step 4: Spot-check DB content**

```bash
sqlite3 policy/catalog/policy_catalog_v2.sqlite \
  "SELECT COUNT(*) FROM policyos_rules; SELECT id,rule_text FROM policyos_rules WHERE id='PLOS-KERN-0001'; SELECT * FROM policyos_pillar_overlays WHERE pillar_slug='healthcare';"
```

Expect: total > 150; KERN-0001 text present; healthcare has KERN mandatory + conditional rows.

- [ ] **Step 5: Verify sentinel in data.js**

```bash
grep -n "POLICYOS-FAMILIES-BEGIN\|POLICYOS-OVERLAYS-BEGIN" docs/assets/js/data.js
```

Expected: two matching lines after line 95.

- [ ] **Step 6: Unit tests still pass**

```bash
npm run test:unit
```

Expected: all tests pass (sentinel additions don't break the eval-based loader).

- [ ] **Step 7: Commit**

```bash
git add scripts/migrate-policyos-to-db.py scripts/requirements.txt \
        docs/assets/js/data.js policy/catalog/policy_catalog_v2.sqlite
git commit -m "feat(policyos): migrate PolicyOS rules to DB + init data.js sentinels

- Add policyos_layers, policyos_families, policyos_rules, policyos_pillar_overlays tables
- Parse System Principles (93 rules), Authoring OS (43 rules), Platform Values (22 rows)
- Load 25-pillar inheritance matrix into overlay table
- Append sentinel comment blocks to data.js for generator to fill

Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"
```

---

## Chunk 2: Generation script + policyos.html

### Task 3: Create `scripts/generate-policyos.py`

**Files:**
- Create: `scripts/generate-policyos.py`
- Creates: `docs/policyos.html`
- Modifies: `docs/assets/js/data.js` (fills sentinel regions)

The generator is idempotent. It fails fast if sentinels are absent (run migration first). The HTML it writes is a complete, self-contained file following the site shell pattern.

- [ ] **Step 1: Write the generation script**

```python
#!/usr/bin/env python3
"""generate-policyos.py

Reads policy_catalog_v2.sqlite and writes:
  - docs/policyos.html (full PolicyOS reference page)
  - Fills %%POLICYOS-FAMILIES-%% and %%POLICYOS-OVERLAYS-%% in data.js

Run from repo root:
  python3 scripts/generate-policyos.py

Migration script must have been run first.
"""
import html
import json
import re
import sqlite3
import sys
from pathlib import Path

try:
    import markdown2
except ImportError:
    print("ERROR: markdown2 not installed. Run: pip install -r scripts/requirements.txt", file=sys.stderr)
    sys.exit(1)

REPO        = Path(__file__).resolve().parent.parent
DB_PATH     = REPO / "policy/catalog/policy_catalog_v2.sqlite"
DATA_JS     = REPO / "docs/assets/js/data.js"
POLICYOS_HTML = REPO / "docs/policyos.html"
GOVERNANCE_MD = REPO / "policy/policyos/policyos_governance_v1.md"

SENTINEL_FAMILIES_RE = re.compile(
    r'(// %%POLICYOS-FAMILIES-BEGIN%%\n).*?(// %%POLICYOS-FAMILIES-END%%)',
    re.DOTALL
)
SENTINEL_OVERLAYS_RE = re.compile(
    r'(// %%POLICYOS-OVERLAYS-BEGIN%%\n).*?(// %%POLICYOS-OVERLAYS-END%%)',
    re.DOTALL
)

# ── Helpers ───────────────────────────────────────────────────────────

def h(text: str) -> str:
    """HTML-escape a string."""
    return html.escape(text or "")


def offset_headings(html_str: str) -> str:
    """Shift h1→h3, h2→h4 in generated markdown HTML."""
    html_str = re.sub(r'<h1\b', '<h3', html_str)
    html_str = re.sub(r'</h1>', '</h3>', html_str)
    html_str = re.sub(r'<h2\b', '<h4', html_str)
    html_str = re.sub(r'</h2>', '</h4>', html_str)
    return html_str


# ── DB queries ────────────────────────────────────────────────────────

def load_data(con: sqlite3.Connection) -> dict:
    cur = con.cursor()

    layers = cur.execute(
        "SELECT id, label, summary FROM policyos_layers ORDER BY sort_order"
    ).fetchall()

    families = cur.execute(
        "SELECT code, layer_id, label, anchor_id, summary FROM policyos_families ORDER BY sort_order"
    ).fetchall()

    rules = cur.execute(
        "SELECT id, family_code, layer_id, sort_order, rule_text, value_name, rule_subtype "
        "FROM policyos_rules ORDER BY layer_id, sort_order"
    ).fetchall()

    overlays = cur.execute(
        "SELECT pillar_slug, family_code, overlay_type FROM policyos_pillar_overlays"
    ).fetchall()

    return {"layers": layers, "families": families, "rules": rules, "overlays": overlays}


# ── data.js sentinel fill ────────────────────────────────────────────

def build_js_families(families: list) -> str:
    """JSON array of System Principles families for JS runtime."""
    js_families = [
        {"code": f[0], "label": f[2], "anchor": f[3], "summary": f[4]}
        for f in families if f[1] == "principles"
    ]
    return json.dumps(js_families, indent=2)


def build_js_overlays(overlays: list) -> str:
    """JS object mapping pillar_slug → [{code, type}]."""
    by_slug: dict = {}
    for slug, fam, otype in overlays:
        by_slug.setdefault(slug, []).append({"code": fam, "type": otype})
    return json.dumps(by_slug, indent=2)


def fill_sentinels(data_js: Path, families_js: str, overlays_js: str) -> None:
    src = data_js.read_text(encoding="utf-8")
    if "%%POLICYOS-FAMILIES-BEGIN%%" not in src:
        print("ERROR: sentinels not found in data.js. Run migrate-policyos-to-db.py first.", file=sys.stderr)
        sys.exit(1)
    src = SENTINEL_FAMILIES_RE.sub(
        r'\g<1>' + f"siteData.policyosFamilies = {families_js};\n" + r'\g<2>',
        src
    )
    src = SENTINEL_OVERLAYS_RE.sub(
        r'\g<1>' + f"siteData.policyosOverlays = {overlays_js};\n" + r'\g<2>',
        src
    )
    data_js.write_text(src, encoding="utf-8")
    print(f"data.js sentinels filled.")


# ── HTML generation ────────────────────────────────────────────────────

def render_values_section(rules: list) -> str:
    """Render the Platform Values layer section."""
    # Group floor/duty rows by value_name in order of appearance
    seen: dict[str, dict] = {}
    for rule in rules:
        _id, _fam, layer_id, _sort, rule_text, value_name, rule_subtype = rule
        if layer_id != "values" or not value_name:
            continue
        if value_name not in seen:
            seen[value_name] = {"floor": "", "duty": ""}
        if rule_subtype == "floor":
            seen[value_name]["floor"] = rule_text
        elif rule_subtype == "duty":
            seen[value_name]["duty"] = rule_text

    parts = []
    for i, (name, content) in enumerate(seen.items(), 1):
        parts.append(f"""
  <div class="plos-value-card">
    <h3 class="plos-value-name">{i}. {h(name)}</h3>
    <div class="plos-floor-duty">
      <div class="plos-floor">
        <strong>Policy-writing floor</strong>
        <p>{h(content['floor'])}</p>
      </div>
      <div class="plos-duty">
        <strong>Policy-writing duty</strong>
        <p>{h(content['duty'])}</p>
      </div>
    </div>
  </div>""")

    return "\n".join(parts)


def render_family_rules(family_code: str, rules: list) -> str:
    """Render all rules for a given family as an ordered list."""
    family_rules = [r for r in rules if r[1] == family_code]
    if not family_rules:
        return "<p><em>No rules found.</em></p>"
    items = []
    for rule in sorted(family_rules, key=lambda r: r[3]):
        rule_id, _, _, _, rule_text, _, _ = rule
        items.append(
            f'<li id="{h(rule_id.lower())}">'
            f'<code class="plos-rule-id">{h(rule_id)}</code> '
            f'{h(rule_text)}</li>'
        )
    return "<ol class=\"plos-rule-list\">\n" + "\n".join(items) + "\n</ol>"


def render_layer_section(layer: tuple, families: list, rules: list) -> str:
    """Render a full layer section (System Principles or Authoring OS)."""
    layer_id, label, summary = layer
    layer_families = [f for f in families if f[1] == layer_id]
    family_blocks = []
    for fam in layer_families:
        code, _, fam_label, anchor_id, fam_summary = fam
        family_blocks.append(f"""
  <details class="plos-family" id="{h(anchor_id)}">
    <summary class="plos-family-summary">
      <span class="plos-family-code">{h(code)}</span>
      <span class="plos-family-label">{h(fam_label)}</span>
    </summary>
    <p class="plos-family-desc">{h(fam_summary)}</p>
    {render_family_rules(code, rules)}
  </details>""")

    return "\n".join(family_blocks)


def render_governance_section() -> str:
    """Convert governance.md to HTML with heading offset."""
    if not GOVERNANCE_MD.exists():
        return "<p><em>Governance document not found.</em></p>"
    md_text = GOVERNANCE_MD.read_text(encoding="utf-8")
    raw = markdown2.markdown(md_text, extras=["fenced-code-blocks"])
    return offset_headings(raw)


def build_html(data: dict) -> str:
    """Build the complete policyos.html string."""
    layers  = data["layers"]
    families = data["families"]
    rules    = data["rules"]

    # Layer 1: Platform Values
    values_layer = next(l for l in layers if l[0] == "values")
    values_html  = render_values_section(rules)

    # Layer 2: System Principles
    principles_layer = next(l for l in layers if l[0] == "principles")
    principles_html  = render_layer_section(principles_layer, families, rules)

    # Layer 3: Authoring OS
    authoring_layer = next(l for l in layers if l[0] == "authoring")
    authoring_html  = render_layer_section(authoring_layer, families, rules)

    # Governance
    governance_html = render_governance_section()

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>PolicyOS — Freedom and Dignity Project</title>
  <meta name="description" content="The meta-layer governing how all policy is written, tested, enforced, and maintained.">
  <link rel="stylesheet" href="assets/css/style.css">
  <style>:root {{ --accent-color: var(--navy); }}</style>
</head>
<body>
<a href="#main-content" class="skip-link sr-only focusable">Skip to main content</a>

<nav class="site-nav" aria-label="Site navigation">
  <div class="wrap nav-inner">
    <a href="index.html" class="nav-brand">Freedom &amp; Dignity</a>
    <ul class="nav-links"></ul>
    <button class="hamburger" aria-label="Open menu" aria-expanded="false">&#9776;</button>
  </div>
</nav>

<main id="main-content">

<section class="pil-hero" style="background:var(--navy)">
  <div class="wrap">
    <h1>PolicyOS</h1>
    <p class="hero-sub">The meta-layer governing how all policy is written, tested, enforced, and maintained across this platform.</p>
    <nav class="plos-layer-nav" aria-label="PolicyOS layers">
      <a href="#plos-values">Layer 1: Platform Values</a>
      <a href="#plos-principles">Layer 2: System Principles</a>
      <a href="#plos-authoring">Layer 3: Authoring OS</a>
      <a href="#plos-governance">Governance</a>
    </nav>
  </div>
</section>

<section id="plos-values" class="bg-parchment ruled">
  <div class="wrap">
    <h2>{h(values_layer[1])}</h2>
    <p>{h(values_layer[2])}</p>
    <p class="plos-status-badge"><span class="clf-badge clf-badge--statute">Locked</span></p>
  </div>
  <div class="wrap plos-values-grid">
    {values_html}
  </div>
</section>

<section id="plos-principles" class="bg-white ruled">
  <div class="wrap">
    <h2>{h(principles_layer[1])}</h2>
    <p>{h(principles_layer[2])}</p>
    <p class="plos-status-badge"><span class="clf-badge clf-badge--statute">Locked</span></p>
    <p class="plos-families-hint">Each family is collapsible. Click a family heading to expand its rules.</p>
  </div>
  <div class="wrap plos-families-list">
    {principles_html}
  </div>
</section>

<section id="plos-authoring" class="bg-parchment ruled">
  <div class="wrap">
    <h2>{h(authoring_layer[1])}</h2>
    <p>{h(authoring_layer[2])}</p>
    <p class="plos-status-badge"><span class="clf-badge clf-badge--statute">Locked</span></p>
  </div>
  <div class="wrap plos-families-list">
    {authoring_html}
  </div>
</section>

<section id="plos-governance" class="bg-white ruled">
  <div class="wrap plos-governance-prose">
    <h2>Governance</h2>
    {governance_html}
  </div>
</section>

</main>

<div class="page-nav-cta">
  <div class="wrap">
    <p>PolicyOS governs how all policy in this platform is designed. See it in action on any pillar page.</p>
    <a href="policy-library.html" class="btn-primary">View Policy Library &#8594;</a>
  </div>
</div>

<footer class="site-footer">
  <div class="wrap">
    <span class="footer-brand">Freedom and Dignity Project</span>
    <ul class="footer-links">
      <li><a href="index.html">Home</a></li>
      <li><a href="platform.html">Platform</a></li>
      <li><a href="rights.html">Rights</a></li>
      <li><a href="about-us.html">About</a></li>
      <li><a href="compare/index.html">Perspectives</a></li>
    </ul>
    <span class="footer-note">Freedom and Dignity Project &middot; <a href="about-ai.html" style="color:inherit;opacity:.7">On the Use of AI</a></span>
  </div>
</footer>
<script src="assets/js/data.js"></script>
<script src="assets/js/app.js"></script>
</body>
</html>
"""


# ── CSS additions (append to style.css) ───────────────────────────────

PLOS_CSS = """
/* ── POLICYOS PAGE ────────────────────────────────────── */
.plos-layer-nav { display: flex; flex-wrap: wrap; gap: .75rem; margin-top: 1.5rem; }
.plos-layer-nav a {
  color: #fff; border: 1px solid rgba(255,255,255,.4); border-radius: 4px;
  padding: .3rem .75rem; font-size: .88rem; text-decoration: none;
}
.plos-layer-nav a:hover { background: rgba(255,255,255,.12); }

.plos-status-badge { margin: -.25rem 0 1rem; }

.plos-values-grid { display: grid; grid-template-columns: 1fr; gap: 1.5rem; }
@media (min-width: 740px) { .plos-values-grid { grid-template-columns: 1fr 1fr; } }

.plos-value-card {
  background: #fff; border: 1px solid var(--rule); border-radius: 8px; padding: 1.25rem;
}
.plos-value-name { font-size: 1.05rem; margin: 0 0 .75rem; color: var(--navy); }
.plos-floor-duty { display: flex; flex-direction: column; gap: .75rem; }
.plos-floor, .plos-duty { background: var(--cream); border-radius: 4px; padding: .75rem 1rem; }
.plos-floor strong { color: #8b5e1a; }
.plos-duty strong  { color: #1a5f3a; }
.plos-floor p, .plos-duty p { margin: .25rem 0 0; font-size: .9rem; }

.plos-families-hint { font-size: .9rem; color: #555; }

.plos-families-list { display: flex; flex-direction: column; gap: .5rem; }

.plos-family {
  border: 1px solid var(--rule); border-radius: 6px; overflow: hidden;
  background: #fff;
}
.plos-family[open] { border-color: var(--navy); }
.plos-family-summary {
  display: flex; align-items: center; gap: .75rem;
  padding: .9rem 1.1rem; cursor: pointer; list-style: none;
  background: var(--cream);
}
.plos-family-summary::-webkit-details-marker { display: none; }
.plos-family-summary::before {
  content: '+'; font-size: 1.1rem; color: var(--navy); width: 1.1rem; text-align: center;
}
details[open] .plos-family-summary::before { content: '\\2212'; }
.plos-family-code {
  font-family: monospace; font-size: .9rem; font-weight: 700;
  background: var(--navy); color: #fff; padding: .1em .45em; border-radius: 3px;
}
.plos-family-label { font-weight: 600; color: var(--navy); }
.plos-family-desc { padding: .75rem 1.1rem .5rem; font-size: .9rem; color: #555; margin: 0; }

.plos-rule-list {
  padding: .5rem 1.1rem 1rem 2.5rem; margin: 0;
  display: flex; flex-direction: column; gap: .6rem;
}
.plos-rule-list li { font-size: .9rem; line-height: 1.55; }
.plos-rule-id {
  font-size: .78rem; background: #f0f0f0; padding: .1em .4em;
  border-radius: 3px; margin-right: .4em; vertical-align: middle;
}

.plos-governance-prose h3 { color: var(--navy); }
.plos-governance-prose h4 { color: #444; }

/* ── PILLAR POLICYOS OVERLAY SECTION ─────────────────── */
#pil-policyos .plos-overlay-list {
  list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: .6rem;
}
#pil-policyos .plos-overlay-list li {
  background: var(--cream); border: 1px solid var(--rule); border-radius: 6px;
  padding: .7rem 1rem; font-size: .9rem;
}
#pil-policyos .plos-overlay-list li strong { color: var(--navy); }
#pil-policyos .plos-overlay-list a { font-size: .85rem; margin-left: .5rem; }
"""


def ensure_plos_css(style_css: Path) -> None:
    """Append PolicyOS CSS to style.css if not already present."""
    src = style_css.read_text(encoding="utf-8")
    if "POLICYOS PAGE" in src:
        print("PolicyOS CSS already in style.css — skipping.")
        return
    style_css.write_text(src + PLOS_CSS, encoding="utf-8")
    print("PolicyOS CSS appended to style.css.")


# ── Main ──────────────────────────────────────────────────────────────

def main() -> None:
    con = sqlite3.connect(DB_PATH)
    data = load_data(con)
    con.close()

    # Fill data.js sentinels
    families_js  = build_js_families(data["families"])
    overlays_js  = build_js_overlays(data["overlays"])
    fill_sentinels(DATA_JS, families_js, overlays_js)

    # Write policyos.html
    html_out = build_html(data)
    POLICYOS_HTML.write_text(html_out, encoding="utf-8")
    print(f"Written: {POLICYOS_HTML}")

    # Append CSS
    style_css = REPO / "docs/assets/css/style.css"
    ensure_plos_css(style_css)


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Run the generator**

```bash
python3 scripts/generate-policyos.py
```

Expected:
```
data.js sentinels filled.
Written: .../docs/policyos.html
PolicyOS CSS appended to style.css.
```

- [ ] **Step 3: Sanity-check the generated HTML**

```bash
grep -c "plos-rule-id\|PLOS-KERN\|PAOS-NORM\|VAL-0001" docs/policyos.html
```

Expected: > 100 matches. Also verify:

```bash
grep "plos-values\|plos-principles\|plos-authoring\|plos-governance" docs/policyos.html
```

Expected: all four section IDs present.

- [ ] **Step 4: Verify data.js sentinel fill**

```bash
node -e "const window={}; eval(require('fs').readFileSync('docs/assets/js/data.js','utf8')); \
  console.log('families:', window.siteData.policyosFamilies.length); \
  console.log('overlays keys:', Object.keys(window.siteData.policyosOverlays).length);"
```

Expected: `families: 11`, `overlays keys: 25`.

- [ ] **Step 5: Run unit tests**

```bash
npm run test:unit
```

Expected: all tests pass.

- [ ] **Step 6: Commit**

```bash
git add scripts/generate-policyos.py docs/policyos.html \
        docs/assets/js/data.js docs/assets/css/style.css
git commit -m "feat(policyos): generate policyos.html and fill data.js sentinels

- Generate full three-layer PolicyOS reference page from DB
- Fill policyosFamilies (11) and policyosOverlays (25) in data.js
- Append PolicyOS and pillar overlay CSS to style.css

Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"
```

---

## Chunk 3: app.js injection + HTML edits

### Task 4: Add PolicyOS nav link to hamburger tree

**Files:**
- Modify: `docs/assets/js/app.js` lines 159–163

- [ ] **Step 1: Add PolicyOS as 4th item in "The Platform" dropdown**

In `app.js`, the "The Platform" children array is at lines 159–163. Add `PolicyOS` after `Platform Overview`:

```js
// Before:
{ label: 'The Platform', children: [
  { label: 'Rights',            href: base + 'rights.html' },
  { label: 'Policy Library',    href: base + 'policy-library.html', children: policyLibraryChildren },
  { label: 'Platform Overview', href: base + 'platform.html' },
]},

// After:
{ label: 'The Platform', children: [
  { label: 'Rights',            href: base + 'rights.html' },
  { label: 'Policy Library',    href: base + 'policy-library.html', children: policyLibraryChildren },
  { label: 'Platform Overview', href: base + 'platform.html' },
  { label: 'PolicyOS',          href: base + 'policyos.html' },
]},
```

- [ ] **Step 2: Verify nav renders (quick E2E smoke check)**

```bash
npm run test:e2e -- --grep "nav"
```

Expected: no regressions.

---

### Task 5: Inject `#pil-policyos` section on pillar pages

**Files:**
- Modify: `docs/assets/js/app.js` (add new IIFE before the final `})();`)

- [ ] **Step 1: Add the pillar overlay injection block**

Add the following immediately before the closing `})();` of app.js (before line 612):

```js
  /* ── POLICYOS PILLAR OVERLAY ─────────────────────── */
  // Injects a PolicyOS design-rules section after #pil-related on pillar pages.
  (function () {
    const related = document.getElementById('pil-related');
    if (!related) return;
    if (!window.siteData || !siteData.policyosOverlays || !siteData.policyosFamilies) return;

    const fileName = location.pathname.split('/').pop();
    const slug = (fileName || '').replace('.html', '').replace(/-/g, '_');

    const pillarOverlays = siteData.policyosOverlays[slug];
    if (!pillarOverlays || !pillarOverlays.length) return;

    const allFamilies = siteData.policyosFamilies;

    function familyMeta(code) {
      return allFamilies.find(function (f) { return f.code === code; }) || {};
    }

    function renderList(items, heading) {
      if (!items.length) return '';
      const base = /\/(pillars|compare)\//.test(location.pathname) ? '../' : '';
      const lis = items.map(function (f) {
        const meta = familyMeta(f.code);
        return '<li><strong>' + f.code + ' \u2014 ' + (meta.label || f.code) + ':</strong> '
          + '<span>' + (meta.summary || '') + '</span> '
          + '<a href="' + base + 'policyos.html#' + (meta.anchor || 'plos-' + f.code.toLowerCase()) + '">View rules \u2192</a></li>';
      }).join('');
      return '<h3>' + heading + '</h3><ul class="plos-overlay-list">' + lis + '</ul>';
    }

    const mandatory   = pillarOverlays.filter(function (f) { return f.type === 'mandatory'; });
    const conditional = pillarOverlays.filter(function (f) { return f.type === 'conditional'; });

    const base = /\/(pillars|compare)\//.test(location.pathname) ? '../' : '';
    const section = document.createElement('section');
    section.className = 'bg-white ruled';
    section.id = 'pil-policyos';
    section.innerHTML =
      '<div class="wrap">'
      + '<h2>PolicyOS Design Rules</h2>'
      + '<p style="font-size:.92rem;color:#666;margin-bottom:.5rem">'
      + 'System design rules that apply to this pillar under the PolicyOS framework.'
      + '</p>'
      + renderList(mandatory, 'Mandatory overlays')
      + renderList(conditional, 'Conditional overlays')
      + '<p style="margin-top:1.5rem"><a href="' + base + 'policyos.html">Full PolicyOS documentation \u2192</a></p>'
      + '</div>';

    related.insertAdjacentElement('afterend', section);

    // Append snav link so scrollspy picks it up
    const snav = document.getElementById('pil-snav');
    if (snav) {
      const ul = snav.querySelector('ul');
      if (ul) {
        const li = document.createElement('li');
        li.innerHTML = '<a href="#pil-policyos">PolicyOS</a>';
        ul.appendChild(li);
      }
    }
  })();
```

- [ ] **Step 2: Run unit tests**

```bash
npm run test:unit
```

Expected: pass.

---

### Task 6: Update `docs/classification.html`

**Files:**
- Modify: `docs/classification.html`

Three changes: (1) System Principles badge line 133 "Under review" → "Locked", (2) Authoring OS badge line 138 "Under review" → "Locked", (3) remove stale paragraph at line 144, (4) add link to policyos.html after the table.

- [ ] **Step 1: Fix System Principles badge (line 133)**

```html
<!-- Before -->
<td><span class="clf-badge clf-badge--policy">Under review</span></td>

<!-- After (System Principles row only) -->
<td><span class="clf-badge clf-badge--statute">Locked</span></td>
```

There are two such changes (one for each of System Principles and Authoring OS). They are adjacent but in separate `<tr>` elements, so make each replacement using the surrounding context to target the right row.

- [ ] **Step 2: Remove stale paragraph (line 144)**

Remove this paragraph entirely:

```html
<p>PolicyOS rules will not be canonicalized into the main platform until the structural review is complete. For the current status and working files, see the <code>policyos/</code> directory in the project repository.</p>
```

- [ ] **Step 3: Add link to policyos.html after the table closing `</div>`**

After `</div>` on line 142 (end of the table wrapper), add:

```html
  <p style="margin-top:1rem">
    <a href="policyos.html">View full PolicyOS documentation &#8594;</a>
  </p>
```

- [ ] **Step 4: Hard-coded count scan + confirmation**

Verify no hard-coded PolicyOS rule counts exist in the main HTML files (the spec flags these as candidates but they turned out to be absent):

```bash
grep -rn "policyos\|PLOS-\|PAOS-" \
  docs/equal-justice-and-policing.html \
  docs/pillars/technology-and-ai.html \
  docs/pillars/foreign-policy.html \
  docs/pillars/science-technology-space.html \
  docs/about-ai.html 2>/dev/null
```

Expected: zero matches (or only unrelated mentions). No changes needed if clean.

- [ ] **Step 5: Commit**

```bash
git add docs/assets/js/app.js docs/classification.html
git commit -m "feat(policyos): wire nav, per-pillar overlay, and classification updates

- Add PolicyOS to hamburger 'The Platform' dropdown
- Inject #pil-policyos section + snav link on pillar pages from data.js
- classification.html: mark System Principles and Authoring OS as Locked
- classification.html: remove stale pre-canonicalization paragraph
- classification.html: add link to policyos.html

Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"
```

---

## Chunk 4: Tests + docs + push

### Task 7: Unit tests

**Files:**
- Modify: `tests/unit/data.test.js`

Add three new `describe` blocks after the existing blocks.

- [ ] **Step 1: Add policyosFamilies tests**

```js
describe('policyosFamilies', function () {
  it('is defined on siteData', function () {
    expect(siteData.policyosFamilies).toBeDefined();
  });

  it('has exactly 11 entries (System Principles only)', function () {
    // 11 PLOS families; Authoring OS families are not included in the JS runtime array
    expect(siteData.policyosFamilies).toHaveLength(11);
  });

  it('every entry has code, label, anchor, and summary', function () {
    siteData.policyosFamilies.forEach(function (f) {
      expect(f.code).toBeTruthy();
      expect(f.label).toBeTruthy();
      expect(f.anchor).toBeTruthy();
      expect(f.summary).toBeTruthy();
    });
  });

  it('KERN is the first family', function () {
    expect(siteData.policyosFamilies[0].code).toBe('KERN');
  });
});

describe('policyosOverlays', function () {
  it('is defined on siteData', function () {
    expect(siteData.policyosOverlays).toBeDefined();
  });

  it('has exactly 25 pillar entries', function () {
    expect(Object.keys(siteData.policyosOverlays)).toHaveLength(25);
  });

  it('every entry is a non-empty array of {code, type} objects', function () {
    Object.values(siteData.policyosOverlays).forEach(function (overlays) {
      expect(overlays.length).toBeGreaterThan(0);
      overlays.forEach(function (o) {
        expect(o.code).toBeTruthy();
        expect(['mandatory', 'conditional']).toContain(o.type);
      });
    });
  });

  it('KERN is mandatory for every pillar', function () {
    Object.entries(siteData.policyosOverlays).forEach(function ([slug, overlays]) {
      const kern = overlays.find(function (o) { return o.code === 'KERN'; });
      expect(kern, slug + ' should have KERN overlay').toBeDefined();
      expect(kern.type).toBe('mandatory');
    });
  });
});
```

- [ ] **Step 2: Run unit tests and confirm they pass**

```bash
npm run test:unit
```

Expected: new describe blocks pass; existing tests unaffected.

---

### Task 8: E2E tests

**Files:**
- Modify: `tests/e2e/site.spec.js`

Add three new `describe` blocks at the end of the file (before the closing of the outer `describe` or directly at top level).

- [ ] **Step 1: Add policyos.html describe block**

```js
describe('policyos.html', function () {
  test('loads with correct title', async function ({ page }) {
    await page.goto('/policyos.html');
    await expect(page).toHaveTitle(/PolicyOS/i);
  });

  test('has all three layer sections', async function ({ page }) {
    await page.goto('/policyos.html');
    await expect(page.locator('#plos-values')).toBeAttached();
    await expect(page.locator('#plos-principles')).toBeAttached();
    await expect(page.locator('#plos-authoring')).toBeAttached();
    await expect(page.locator('#plos-governance')).toBeAttached();
  });

  test('nav includes PolicyOS link', async function ({ page }) {
    await page.goto('/policyos.html');
    // Hamburger tree renders in hidden nav; open it to expose the item
    await page.locator('.hamburger').click();
    await expect(page.locator('.hamburger-tree a[href*="policyos"]')).toBeAttached();
  });

  test('Platform Values section has value cards', async function ({ page }) {
    await page.goto('/policyos.html');
    await expect(page.locator('.plos-value-card').first()).toBeAttached();
    const count = await page.locator('.plos-value-card').count();
    // 11 platform values
    expect(count).toBe(11);
  });

  test('System Principles has collapsible family details', async function ({ page }) {
    await page.goto('/policyos.html');
    await expect(page.locator('#plos-principles details.plos-family').first()).toBeAttached();
    const count = await page.locator('#plos-principles details.plos-family').count();
    expect(count).toBe(11);
  });

  test('Authoring OS has 6 collapsible family details', async function ({ page }) {
    await page.goto('/policyos.html');
    const count = await page.locator('#plos-authoring details.plos-family').count();
    expect(count).toBe(6);
  });

  test('expanding a family shows its rules', async function ({ page }) {
    await page.goto('/policyos.html');
    const kern = page.locator('#plos-kern');
    await kern.click();  // click summary to open
    await expect(page.locator('#plos-kern ol.plos-rule-list li').first()).toBeVisible();
  });
});
```

- [ ] **Step 2: Add per-pillar overlay injection test**

```js
describe('pillar PolicyOS overlay', function () {
  test('#pil-policyos section is injected after #pil-related', async function ({ page }) {
    await page.goto('/pillars/healthcare.html');
    await expect(page.locator('#pil-policyos')).toBeAttached();

    // Assert DOM order: #pil-related must appear before #pil-policyos
    const isAfterRelated = await page.evaluate(function () {
      const related = document.getElementById('pil-related');
      const overlay  = document.getElementById('pil-policyos');
      if (!related || !overlay) return false;
      return !!(related.compareDocumentPosition(overlay) & Node.DOCUMENT_POSITION_FOLLOWING);
    });
    expect(isAfterRelated).toBe(true);
  });

  test('snav gains a PolicyOS link', async function ({ page }) {
    await page.goto('/pillars/healthcare.html');
    await expect(page.locator('#pil-snav a[href="#pil-policyos"]')).toBeAttached();
  });

  test('#pil-policyos has at least one overlay family listed', async function ({ page }) {
    await page.goto('/pillars/healthcare.html');
    await expect(page.locator('#pil-policyos .plos-overlay-list li').first()).toBeAttached();
  });
});
```

- [ ] **Step 3: Add classification.html badge test**

```js
describe('classification.html PolicyOS status', function () {
  test('System Principles badge is Locked', async function ({ page }) {
    await page.goto('/classification.html');
    const rows = page.locator('tbody tr');
    const systemPrinciplesRow = rows.filter({ hasText: 'System Principles' });
    await expect(systemPrinciplesRow.locator('.clf-badge')).toHaveText('Locked');
  });

  test('Authoring OS badge is Locked', async function ({ page }) {
    await page.goto('/classification.html');
    const rows = page.locator('tbody tr');
    const authoringRow = rows.filter({ hasText: 'Authoring OS' });
    await expect(authoringRow.locator('.clf-badge')).toHaveText('Locked');
  });

  test('link to policyos.html is present', async function ({ page }) {
    await page.goto('/classification.html');
    await expect(page.locator('a[href="policyos.html"]')).toBeAttached();
  });
});
```

- [ ] **Step 4: Run full E2E suite**

```bash
npm run test:e2e
```

Expected: all existing tests pass; new tests pass. If anything fails, debug before proceeding.

---

### Task 9: Update README.md

**Files:**
- Modify: `README.md`

Add two rows to the Scripts table (lines 64–70):

```markdown
| `python3 scripts/migrate-policyos-to-db.py` | One-time: parse PolicyOS markdown + CSV into DB tables; init data.js sentinels |
| `python3 scripts/generate-policyos.py` | Regenerate `docs/policyos.html` and fill `data.js` PolicyOS sentinels from DB |
```

---

### Task 10: Final commit and push

- [ ] **Step 1: Run full test suite one last time**

```bash
npm run test:unit && npm run test:e2e
```

Expected: all pass.

- [ ] **Step 2: Commit docs + tests**

```bash
git add tests/unit/data.test.js tests/e2e/site.spec.js README.md
git commit -m "test(policyos): add unit + E2E tests for policyos.html, overlay injection, classification

- 3 unit test describe blocks: policyosFamilies shape, overlays shape, KERN invariant
- E2E: policyos.html loads/renders 3 layers + 17 families + governance
- E2E: pillar overlay injection + DOM order + snav link (healthcare)
- E2E: classification.html badges Locked + link to policyos.html
- README: add migrate-policyos-to-db.py and generate-policyos.py to Scripts table

Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"
```

- [ ] **Step 3: Push**

```bash
git push origin main
```

Expected: push succeeds; GitHub Pages deploys automatically.

- [ ] **Step 4: Verify live site**

After ~2 minutes for GH Pages deployment:
- https://alistardust.github.io/freedom-and-dignity-project/policyos.html loads
- Classification page shows Locked badges + PolicyOS link
- Any pillar page shows `#pil-policyos` section when scrolled down

---

## Implementation notes

### Script execution order (mandatory)

```bash
pip install -r scripts/requirements.txt  # once
python3 scripts/migrate-policyos-to-db.py  # always before generate
python3 scripts/generate-policyos.py        # fills sentinels + writes HTML
```

The generate script exits with code 1 and an error message if the sentinels are absent, enforcing the order.

### Re-running after markdown source changes

If any of the three PolicyOS markdown files change:
1. Re-run `migrate-policyos-to-db.py` (idempotent — uses INSERT OR REPLACE)
2. Re-run `generate-policyos.py`
3. Commit the updated `docs/policyos.html` and `docs/assets/js/data.js`
4. Do NOT hand-edit `docs/policyos.html`

### Pillar slug mapping

The inheritance matrix CSV uses underscores (`healthcare`, `executive_power`). The generator converts pillar filename hyphens to underscores at lookup time: `executive-power.html` → `executive_power`. This is handled in the app.js injection: `fileName.replace(/-/g, '_')`.

### CSS

All PolicyOS styles are in `docs/assets/css/style.css` under the `POLICYOS PAGE` block. No inline styles are added to `docs/policyos.html` beyond the single `--accent-color` declaration in `<style>`.

### SQLite FKs

`PRAGMA foreign_keys = ON` is set at connection open time in the migration script. The overlay family-code validation is done at application layer (pre-insert check) rather than via a DB `CHECK` constraint, because `CHECK (col IN (SELECT ...))` raises `OperationalError: subqueries prohibited in CHECK constraints` in SQLite.
