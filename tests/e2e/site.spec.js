/**
 * Playwright E2E tests — American Renewal Project
 * Browser: Firefox (isolated profile, never touches your existing Firefox)
 * Requires: `npm run serve` or the webServer config in playwright.config.js handles it.
 */

const { test, expect } = require('@playwright/test');

// ── HOMEPAGE ─────────────────────────────────────────────────────────────────

test.describe('Homepage (index.html)', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/');
  });

  test('has correct page title', async ({ page }) => {
    await expect(page).toHaveTitle(/American Renewal/i);
  });

  test('displays the core quote without quotation marks', async ({ page }) => {
    const text = await page.locator('text=You can\'t be free if you\'re sick, homeless, or in debt').first();
    await expect(text).toBeVisible();
    // Verify it's not wrapped in <q> or literal quote marks
    const content = await page.locator('.hero-statement.strong').textContent();
    expect(content).not.toMatch(/^[""\u201C]/);
  });

  test('renders the Remember section', async ({ page }) => {
    await expect(page.locator('text=Remember When Things Felt Real')).toBeVisible();
  });

  test('renders the FDR block with his quote', async ({ page }) => {
    await expect(page.locator('.fdr-block')).toBeVisible();
    await expect(page.locator('text=Necessitous men are not free men')).toBeVisible();
  });

  test('renders all 8 FDR rights', async ({ page }) => {
    const rights = page.locator('.fdr-rights li');
    await expect(rights).toHaveCount(8);
  });

  test('renders all 5 foundation cards', async ({ page }) => {
    const cards = page.locator('.foundations-grid .f-card');
    await expect(cards).toHaveCount(5);
  });

  test('renders the 10 demands list', async ({ page }) => {
    const items = page.locator('.demand-list li');
    await expect(items).toHaveCount(10);
  });

  test('nav has 4 links', async ({ page }) => {
    const links = page.locator('.nav-links a');
    await expect(links).toHaveCount(4);
  });
});

// ── FOUNDATIONS PAGE ──────────────────────────────────────────────────────────

test.describe('Foundations page', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/foundations.html');
  });

  test('has correct page title', async ({ page }) => {
    await expect(page).toHaveTitle(/Foundations/i);
  });

  test('renders all 5 foundation sections', async ({ page }) => {
    const sections = page.locator('section[id]');
    await expect(sections).toHaveCount(5);
  });

  test('each foundation section has an id', async ({ page }) => {
    const expectedIds = [
      'accountable-power', 'clean-democracy', 'equal-justice',
      'real-freedom', 'freedom-to-thrive'
    ];
    for (const id of expectedIds) {
      await expect(page.locator(`#${id}`)).toBeVisible();
    }
  });

  test('displays the core quote', async ({ page }) => {
    await expect(page.locator('text=You can\'t be free if you\'re sick, homeless, or in debt')).toBeVisible();
  });

  test('each foundation has a demands block and rejects block', async ({ page }) => {
    const blocks = page.locator('.f-block');
    // 5 foundations × 2 blocks each = 10
    await expect(blocks).toHaveCount(10);
  });

  test('Explore All Pillars CTA links to pillars.html', async ({ page }) => {
    const cta = page.locator('a.btn-primary');
    await expect(cta).toHaveAttribute('href', 'pillars.html');
  });
});

// ── PILLARS PAGE ──────────────────────────────────────────────────────────────

test.describe('Pillars page', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/pillars.html');
  });

  test('has correct page title', async ({ page }) => {
    await expect(page).toHaveTitle(/Pillars/i);
  });

  test('renders 17 pillar cards', async ({ page }) => {
    await page.waitForSelector('.pillar-card');
    const cards = page.locator('.pillar-card');
    await expect(cards).toHaveCount(17);
  });

  test('renders 6 filter buttons (All + 5 foundations)', async ({ page }) => {
    await page.waitForSelector('.pillar-filter-btn');
    const btns = page.locator('.pillar-filter-btn');
    await expect(btns).toHaveCount(6);
  });

  test('"All Pillars" filter button is active by default', async ({ page }) => {
    await page.waitForSelector('.pillar-filter-btn.active');
    const active = page.locator('.pillar-filter-btn.active');
    await expect(active).toHaveCount(1);
    await expect(active).toHaveText('All Pillars');
  });

  test('filtering by Accountable Power shows only its pillars', async ({ page }) => {
    await page.waitForSelector('.pillar-filter-btn');
    await page.locator('.pillar-filter-btn', { hasText: 'Accountable Power' }).click();
    await page.waitForTimeout(200);
    const cards = page.locator('.pillar-card');
    // Accountable Power has 5 pillars per data.js
    await expect(cards).toHaveCount(5);
  });

  test('filtering by Freedom to Thrive shows 3 pillars', async ({ page }) => {
    await page.waitForSelector('.pillar-filter-btn');
    await page.locator('.pillar-filter-btn', { hasText: 'Freedom to Thrive' }).click();
    await page.waitForTimeout(200);
    const cards = page.locator('.pillar-card');
    await expect(cards).toHaveCount(3);
  });

  test('clicking All after a filter restores 17 cards', async ({ page }) => {
    await page.waitForSelector('.pillar-filter-btn');
    await page.locator('.pillar-filter-btn', { hasText: 'Clean Democracy' }).click();
    await page.waitForTimeout(200);
    await page.locator('.pillar-filter-btn', { hasText: 'All Pillars' }).click();
    await page.waitForTimeout(200);
    await expect(page.locator('.pillar-card')).toHaveCount(17);
  });
});

// ── COMPARE INDEX ─────────────────────────────────────────────────────────────

test.describe('Compare index page', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/compare/index.html');
  });

  test('has correct page title', async ({ page }) => {
    await expect(page).toHaveTitle(/Comparison|Compare/i);
  });

  test('shows all 6 party comparison cards/links', async ({ page }) => {
    const parties = [
      'Democratic Party', 'Republican Party', 'Libertarian',
      'Democratic Socialists', 'Working Families', 'Green Party'
    ];
    for (const party of parties) {
      await expect(page.locator(`text=${party}`).first()).toBeVisible();
    }
  });
});

// ── COMPARE PARTY PAGES ───────────────────────────────────────────────────────

const partyPages = [
  { file: 'democratic-party.html',    name: 'Democratic Party' },
  { file: 'republican-party.html',    name: 'Republican Party' },
  { file: 'libertarian-party.html',   name: 'Libertarian' },
  { file: 'dsa.html',                 name: 'Democratic Socialists' },
  { file: 'working-families-party.html', name: 'Working Families' },
  { file: 'green-party.html',         name: 'Green Party' },
];

for (const { file, name } of partyPages) {
  test.describe(`Compare: ${name}`, () => {
    test.beforeEach(async ({ page }) => {
      await page.goto(`/compare/${file}`);
    });

    test('loads without error', async ({ page }) => {
      await expect(page.locator('.site-nav')).toBeVisible();
    });

    test('has a coverage/gap section', async ({ page }) => {
      // All compare pages should have some coverage grid or table
      const hasCoverage = await page.locator('[class*="cov"], [class*="coverage"], [class*="gap"]').count();
      expect(hasCoverage).toBeGreaterThan(0);
    });

    test('back link navigates to compare index', async ({ page }) => {
      const backLink = page.locator('a[href="index.html"], a[href*="compare/index"]').first();
      await expect(backLink).toBeVisible();
    });

    test('does not mention coalition', async ({ page }) => {
      const body = await page.locator('body').textContent();
      expect(body.toLowerCase()).not.toContain('coalition likelihood');
      expect(body.toLowerCase()).not.toContain('coalition score');
    });
  });
}

// ── NAV ───────────────────────────────────────────────────────────────────────

test.describe('Navigation', () => {
  test('nav links work from homepage', async ({ page }) => {
    await page.goto('/');
    await page.click('a[href="foundations.html"]');
    await expect(page).toHaveURL(/foundations/);
  });

  test('nav links work from foundations to pillars', async ({ page }) => {
    await page.goto('/foundations.html');
    await page.click('a[href="pillars.html"]');
    await expect(page).toHaveURL(/pillars/);
  });

  test('nav links work from pillars to compare', async ({ page }) => {
    await page.goto('/pillars.html');
    await page.click('a[href="compare/index.html"]');
    await expect(page).toHaveURL(/compare/);
  });
});
