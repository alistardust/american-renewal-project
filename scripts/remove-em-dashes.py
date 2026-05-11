#!/usr/bin/env python3
"""
Remove em-dashes from body copy of all Nunjucks templates in src/pages/.

Rules:
  1. <span...>— text  →  <span...>text   (strip leading dash from related-card spans)
  2. short-label — description  →  short-label: description
     (text before dash is ≤2 words, or is empty/whitespace after a closing inline tag)
  3. prose — prose  →  prose, prose      (all other spaced em-dashes)
  4. text—text  →  text, text            (no-space em-dash)

Protected (never modified):
  - Content between {% block title %} ... {% endblock %}
  - HTML comments <!-- ... -->
  - href and src attribute values
"""

import os
import re
import sys

EM = "\u2014"  # em-dash


def count_label_words(seg: str) -> int:
    """Count words in seg, stripping emoji and HTML comment delimiters."""
    # Remove emoji characters
    cleaned = re.sub(
        r"[\U00002600-\U000027BF\U0001F000-\U0001FAFF\U0001F300-\U0001F9FF]",
        "",
        seg,
    )
    # Remove HTML comment delimiters so they don't inflate the word count
    cleaned = cleaned.replace("<!--", "").replace("-->", "").strip()
    if not cleaned:
        return 0
    return len(cleaned.split())


def pick_replacement(text: str, match_start: int) -> str:
    """
    Given the text being processed and the position of a ' — ' match,
    decide whether to use ': ' or ', '.

    Strategy: look at the text between the last HTML tag boundary (or last
    em-dash boundary) and the match position.
      - empty / whitespace → closing inline tag preceded the dash → ': '
      - ≤2 words           → short label                          → ': '
      - >2 words           → prose clause                         → ', '
    """
    pre = text[:match_start]

    last_gt = pre.rfind(">")

    if last_gt != -1:
        seg = pre[last_gt + 1 :]
        if not seg.strip():
            # Nothing between the closing tag and the dash: label-in-tag pattern
            # e.g. </strong> — description
            return ": "
        # Handle multiple ' — ' on the same line: look only at text since
        # the last em-dash within this segment.
        last_ed = seg.rfind(EM)
        sub = seg[last_ed + 1 :].strip() if last_ed != -1 else seg.strip()
    else:
        last_ed = pre.rfind(EM)
        sub = pre[last_ed + 1 :].strip() if last_ed != -1 else pre.strip()

    return ": " if count_label_words(sub) <= 2 else ", "


def process_segment(segment: str) -> tuple[str, int]:
    """
    Apply em-dash replacements to an unprotected text segment.
    Returns (modified_text, replacement_count).
    """
    count = 0

    # Case 1: <span...>— text  →  <span...>text
    def span_sub(m: re.Match) -> str:
        nonlocal count
        count += 1
        return m.group(1)

    segment = re.sub(r"(<span[^>]*>)" + EM + r" ", span_sub, segment)

    # Cases 2/3: ' — ' with spaces around the em-dash
    # The callback closes over the *current* value of `segment` (post case-1).
    def spaced_sub(m: re.Match) -> str:
        nonlocal count, segment
        count += 1
        return pick_replacement(segment, m.start())

    segment = re.sub(" " + EM + " ", spaced_sub, segment)

    # Case 4: bare em-dash with no surrounding spaces
    bare_count = segment.count(EM)
    if bare_count:
        count += bare_count
        segment = segment.replace(EM, ", ")

    return segment, count


# Regex that matches regions that must NOT be modified.
# HTML comments are processed for em-dashes (they appear in built HTML and must pass tests),
# so they are NOT protected here.
PROTECTED_RE = re.compile(
    r"(\{%-?\s*block\s+title\s*-?%\}.*?\{%-?\s*endblock\s*-?%\})"  # title block
    r"|(?:href|src)=\"[^\"]*\"",  # href / src attribute values
    re.DOTALL,
)


def process_file(content: str) -> tuple[str, int]:
    """Process a full NJK file, returning (modified_content, total_replacements)."""
    total = 0
    parts: list[str] = []
    prev_end = 0

    for m in PROTECTED_RE.finditer(content):
        if prev_end < m.start():
            processed, n = process_segment(content[prev_end : m.start()])
            parts.append(processed)
            total += n
        parts.append(content[m.start() : m.end()])  # keep protected as-is
        prev_end = m.end()

    if prev_end < len(content):
        processed, n = process_segment(content[prev_end:])
        parts.append(processed)
        total += n

    return "".join(parts), total


def main() -> None:
    src_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src", "pages"
    )

    if not os.path.isdir(src_dir):
        print(f"ERROR: src/pages directory not found at {src_dir}", file=sys.stderr)
        sys.exit(1)

    files_processed = 0
    grand_total = 0
    file_counts: list[tuple[int, str]] = []

    for root, _dirs, filenames in os.walk(src_dir):
        for filename in sorted(filenames):
            if not filename.endswith(".njk"):
                continue
            filepath = os.path.join(root, filename)
            rel = os.path.relpath(filepath, src_dir)

            with open(filepath, encoding="utf-8") as fh:
                original = fh.read()

            modified, count = process_file(original)

            if modified != original:
                with open(filepath, "w", encoding="utf-8") as fh:
                    fh.write(modified)
                files_processed += 1
                grand_total += count
                file_counts.append((count, rel))

    file_counts.sort(reverse=True)
    print(f"\nEm-dash replacements by file (top 20):")
    for n, rel in file_counts[:20]:
        print(f"  {n:6d}  {rel}")

    print(f"\nFiles modified : {files_processed}")
    print(f"Total replacements: {grand_total}")


if __name__ == "__main__":
    main()
