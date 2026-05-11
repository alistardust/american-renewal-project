import { describe, it, expect } from 'vitest';
import { extractCardBlocks, parseCards } from '../../../scripts/backfill-rule-notes.js';

describe('extractCardBlocks', () => {
  it('extracts a single card block', () => {
    const content = '<div class="policy-card" id="TEST-CARD-0001"><p>Content</p></div>';
    const blocks = extractCardBlocks(content);
    expect(blocks).toHaveLength(1);
    expect(blocks[0]).toContain('TEST-CARD-0001');
  });

  it('handles nested divs correctly', () => {
    const content = '<div class="policy-card" id="TEST-NEST-0001"><div class="rule-header"><div class="inner"></div></div></div>';
    const blocks = extractCardBlocks(content);
    expect(blocks).toHaveLength(1);
    expect(blocks[0]).toContain('TEST-NEST-0001');
  });

  it('extracts multiple card blocks', () => {
    const content = `
      <div class="policy-card" id="TEST-MULT-0001"><p>A</p></div>
      <div class="policy-card" id="TEST-MULT-0002"><p>B</p></div>
    `;
    const blocks = extractCardBlocks(content);
    expect(blocks).toHaveLength(2);
  });

  it('returns empty array when no cards present', () => {
    expect(extractCardBlocks('<p>No cards here</p>')).toHaveLength(0);
  });
});

describe('parseCards', () => {
  it('extracts rule-notes from a card', () => {
    const content = '<div class="policy-card" id="HLTH-COVR-0001"><p class="rule-notes">Notes here.</p></div>';
    const cards = parseCards(content);
    expect(cards).toHaveLength(1);
    expect(cards[0].id).toBe('HLTH-COVR-0001');
    expect(cards[0].ruleNotes).toBe('Notes here.');
  });

  it('skips proposal cards (those with rule-body)', () => {
    const content = '<div class="policy-card" id="HLTH-COVR-0002"><p class="rule-body">Body.</p><p class="rule-notes">Notes.</p></div>';
    expect(parseCards(content)).toHaveLength(0);
  });

  it('skips cards without rule-notes', () => {
    const content = '<div class="policy-card" id="HLTH-COVR-0003"><p class="rule-stmt">Stmt.</p></div>';
    expect(parseCards(content)).toHaveLength(0);
  });

  it('skips cards without an id', () => {
    const content = '<div class="policy-card"><p class="rule-notes">Notes.</p></div>';
    expect(parseCards(content)).toHaveLength(0);
  });
});
