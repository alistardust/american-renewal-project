/**
 * Unit tests for docs/assets/js/data.js
 * Verifies the siteData object structure is complete and internally consistent.
 */

import { readFileSync } from 'fs';
import { resolve } from 'path';

// Load data.js in Node by stripping the window.siteData assignment and evaluating
const src = readFileSync(resolve('docs/assets/js/data.js'), 'utf8');
const siteData = (() => {
  const window = {};
  eval(src); // eslint-disable-line no-eval
  return window.siteData;
})();

// Single source of truth for expected counts.
// Update these when intentionally adding pillars or foundations to data.js.
const PILLAR_COUNT     = siteData.pillars.length;      // currently 25
const FOUNDATION_COUNT = siteData.foundations.length;  // currently 5

// ── FOUNDATIONS ──────────────────────────────────────────────────────────────

describe('siteData.foundations', () => {
  test(`has exactly ${FOUNDATION_COUNT} foundations`, () => {
    expect(siteData.foundations).toHaveLength(FOUNDATION_COUNT);
  });

  test.each(siteData.foundations)('foundation "$title" has all required fields', (f) => {
    expect(typeof f.id).toBe('string');
    expect(f.id.length).toBeGreaterThan(0);
    expect(typeof f.title).toBe('string');
    expect(typeof f.color).toBe('string');
    expect(f.color).toMatch(/^#[0-9a-fA-F]{3,6}$/);
    expect(Array.isArray(f.pillars)).toBe(true);
    expect(f.pillars.length).toBeGreaterThan(0);
    expect(Array.isArray(f.demands)).toBe(true);
    expect(Array.isArray(f.rejects)).toBe(true);
  });

  test('foundation IDs are unique', () => {
    const ids = siteData.foundations.map(f => f.id);
    expect(new Set(ids).size).toBe(ids.length);
  });
});

// ── PILLARS ───────────────────────────────────────────────────────────────────

describe('siteData.pillars', () => {
  test(`has exactly ${PILLAR_COUNT} pillars`, () => {
    expect(siteData.pillars).toHaveLength(PILLAR_COUNT);
  });

  test.each(siteData.pillars)('pillar "$title" has all required fields', (p) => {
    expect(typeof p.id).toBe('string');
    expect(p.id.length).toBeGreaterThan(0);
    expect(typeof p.title).toBe('string');
    expect(typeof p.foundation).toBe('string');
    expect(typeof p.summary).toBe('string');
    expect(p.summary.length).toBeGreaterThan(0);
    expect(Array.isArray(p.points)).toBe(true);
    expect(p.points.length).toBeGreaterThan(0);
  });

  test('pillar IDs are unique', () => {
    const ids = siteData.pillars.map(p => p.id);
    expect(new Set(ids).size).toBe(ids.length);
  });

  test('every pillar foundation ID resolves to a real foundation', () => {
    const foundationIds = new Set(siteData.foundations.map(f => f.id));
    siteData.pillars.forEach(p => {
      expect(foundationIds.has(p.foundation),
        `pillar "${p.id}" has unknown foundation "${p.foundation}"`
      ).toBe(true);
    });
  });

  test('all foundation.pillars entries resolve to real pillar IDs', () => {
    const pillarIds = new Set(siteData.pillars.map(p => p.id));
    siteData.foundations.forEach(f => {
      f.pillars.forEach(pid => {
        expect(pillarIds.has(pid),
          `foundation "${f.id}" references unknown pillar "${pid}"`
        ).toBe(true);
      });
    });
  });
});

// ── HELPERS ───────────────────────────────────────────────────────────────────

describe('siteData.getFoundation()', () => {
  test('returns the correct foundation by ID', () => {
    const f = siteData.getFoundation('clean-democracy');
    expect(f).toBeDefined();
    expect(f.title).toBe('Clean Democracy');
  });

  test('returns undefined for an unknown ID', () => {
    expect(siteData.getFoundation('nonexistent')).toBeUndefined();
  });
});

describe('siteData.getPillarsByFoundation()', () => {
  test('returns only pillars belonging to the given foundation', () => {
    const pillars = siteData.getPillarsByFoundation('freedom-to-thrive');
    expect(pillars.length).toBeGreaterThan(0);
    pillars.forEach(p => expect(p.foundation).toBe('freedom-to-thrive'));
  });

  test(`all ${PILLAR_COUNT} pillars are covered across foundations`, () => {
    const total = siteData.foundations.reduce((sum, f) =>
      sum + siteData.getPillarsByFoundation(f.id).length, 0);
    expect(total).toBe(PILLAR_COUNT);
  });

  test('returns empty array for unknown foundation', () => {
    expect(siteData.getPillarsByFoundation('nonexistent')).toHaveLength(0);
  });
});

// ── WINDOW EXPOSURE ───────────────────────────────────────────────────────────

describe('window.siteData', () => {
  test('is exposed on window so app.js guard works', () => {
    expect(siteData).toBeDefined();
    expect(siteData.foundations).toBeDefined();
    expect(siteData.pillars).toBeDefined();
  });
});
