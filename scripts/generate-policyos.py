#!/usr/bin/env python3
"""generate-policyos.py

Reads policy_catalog_v2.sqlite and writes:
  - src/pages/policyos.njk (content block for PolicyOS reference page)
  - Fills %%POLICYOS-FAMILIES-%% and %%POLICYOS-OVERLAYS-%% in data.js

Run from repo root:
  python3 scripts/generate-policyos.py && npm run build

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

REPO            = Path(__file__).resolve().parent.parent
DB_PATH         = REPO / "policy/catalog/policy_catalog_v2.sqlite"
DATA_JS         = REPO / "docs/assets/js/data.js"
POLICYOS_NJK    = REPO / "src/pages/policyos.njk"
GOVERNANCE_MD   = REPO / "policy/policyos/policyos_governance_v1.md"

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
    """Shift h1->h3, h2->h4 in generated markdown HTML."""
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
    """JS object mapping pillar_slug to [{code, type}] array."""
    by_slug: dict = {}
    for slug, fam, otype in overlays:
        by_slug.setdefault(slug, []).append({"code": fam, "type": otype})
    return json.dumps(by_slug, indent=2)


def fill_sentinels(data_js: Path, families_js: str, overlays_js: str) -> None:
    src = data_js.read_text(encoding="utf-8")
    if "%%POLICYOS-FAMILIES-BEGIN%%" not in src:
        print("ERROR: FAMILIES sentinel not found in data.js. Run migrate-policyos-to-db.py first.", file=sys.stderr)
        sys.exit(1)
    if "%%POLICYOS-OVERLAYS-BEGIN%%" not in src:
        print("ERROR: OVERLAYS sentinel not found in data.js. Run migrate-policyos-to-db.py first.", file=sys.stderr)
        sys.exit(1)

    new_families = f"siteData.policyosFamilies = {families_js};\n"
    src = SENTINEL_FAMILIES_RE.sub(
        lambda m: m.group(1) + new_families + m.group(2),
        src
    )

    new_overlays = f"siteData.policyosOverlays = {overlays_js};\n"
    src = SENTINEL_OVERLAYS_RE.sub(
        lambda m: m.group(1) + new_overlays + m.group(2),
        src
    )

    data_js.write_text(src, encoding="utf-8")
    print("data.js sentinels filled.")


# ── HTML generation ────────────────────────────────────────────────────

def render_values_section(rules: list) -> str:
    """Render the Platform Values layer section."""
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
    return '<ol class="plos-rule-list">\n' + "\n".join(items) + "\n</ol>"


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
    """Convert governance.md to HTML with heading offset. Exits 1 if file missing."""
    if not GOVERNANCE_MD.exists():
        print(f"ERROR: governance file not found: {GOVERNANCE_MD}", file=sys.stderr)
        sys.exit(1)
    md_text = GOVERNANCE_MD.read_text(encoding="utf-8")
    raw = markdown2.markdown(md_text, extras=["fenced-code-blocks"])
    return offset_headings(raw)


def build_content_block(data: dict) -> str:
    """Build the content block for the .njk file (no DOCTYPE, no full HTML shell)."""
    layers   = data["layers"]
    families = data["families"]
    rules    = data["rules"]

    values_layer     = next(l for l in layers if l[0] == "values")
    values_html      = render_values_section(rules)

    principles_layer = next(l for l in layers if l[0] == "principles")
    principles_html  = render_layer_section(principles_layer, families, rules)

    authoring_layer  = next(l for l in layers if l[0] == "authoring")
    authoring_html   = render_layer_section(authoring_layer, families, rules)

    governance_html  = render_governance_section()

    return f"""
<section class="pil-hero" style="background:var(--navy)">
  <div class="wrap">
    <h1>PolicyOS</h1>
    <p class="hero-sub" style="color:rgba(255,255,255,.75)">The meta-layer governing how all policy is written, tested, enforced, and maintained across this platform.</p>
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
        print("PolicyOS CSS already in style.css -- skipping.")
        return
    style_css.write_text(src + PLOS_CSS, encoding="utf-8")
    print("PolicyOS CSS appended to style.css.")


# ── Main ──────────────────────────────────────────────────────────────

def main() -> None:
    con = sqlite3.connect(DB_PATH)
    data = load_data(con)
    con.close()

    families_js = build_js_families(data["families"])
    overlays_js = build_js_overlays(data["overlays"])
    fill_sentinels(DATA_JS, families_js, overlays_js)

    content_block = build_content_block(data)
    
    # Build the .njk file with Nunjucks wrapper
    njk_out = f"""{{# AUTO-GENERATED by generate-policyos.py — do not edit directly.
   Run: python3 scripts/migrate-policyos-to-db.py && python3 scripts/generate-policyos.py && npm run build #}}
{{% extends "_base.njk" %}}
{{% set description = "The PolicyOS framework — the cross-platform rules layer for all Freedom and Dignity policy." %}}
{{% set body_class = "policyos" %}}
{{% block title %}}PolicyOS — Freedom and Dignity Project{{% endblock %}}
{{% block og_title %}}PolicyOS — Freedom and Dignity Project{{% endblock %}}
{{% block og_url %}}policyos.html{{% endblock %}}
{{% block content %}}{content_block}
{{% endblock %}}
"""
    
    POLICYOS_NJK.write_text(njk_out, encoding="utf-8")
    print(f"Written: {POLICYOS_NJK}")

    style_css = REPO / "docs/assets/css/style.css"
    ensure_plos_css(style_css)


if __name__ == "__main__":
    main()
