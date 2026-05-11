/**
 * Content quality tests for the built site.
 * Scans docs/ HTML output to catch prohibited text patterns.
 *
 * Em-dashes (— &mdash; &#8212;) are prohibited in body copy.
 * Exception: <title> elements, where "Page — Site Name" is the approved format.
 */
import { readFileSync, readdirSync, statSync } from 'fs';
import { join } from 'path';

function walkHtml(dir) {
  const results = [];
  for (const entry of readdirSync(dir)) {
    if (entry === 'superpowers') continue; // exclude untracked dev-only directory
    const fullPath = join(dir, entry);
    if (statSync(fullPath).isDirectory()) {
      results.push(...walkHtml(fullPath));
    } else if (entry.endsWith('.html')) {
      results.push(fullPath);
    }
  }
  return results;
}

/** Strip <title>...</title> content so approved page titles don't trigger the check. */
function stripTitles(html) {
  return html.replace(/<title>[^<]*<\/title>/gi, '<title></title>');
}

const HTML_FILES = walkHtml('docs');

describe('no em-dashes in body copy', () => {
  it('finds HTML files to test', () => {
    expect(HTML_FILES.length).toBeGreaterThan(0);
  });

  for (const file of HTML_FILES) {
    it(`${file} has no em-dash characters or entities`, () => {
      const body = stripTitles(readFileSync(file, 'utf8'));
      // Unicode em-dash
      expect(body).not.toMatch(/—/);
      // HTML entities for em-dash
      expect(body).not.toMatch(/&mdash;/i);
      expect(body).not.toMatch(/&#8212;/);
      expect(body).not.toMatch(/&#x2014;/i);
    });
  }
});
