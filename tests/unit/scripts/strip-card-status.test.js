import { describe, it, expect } from 'vitest';
import { stripStatusMarkersFromContent } from '../../../scripts/strip-card-status.js';

describe('stripStatusMarkersFromContent', () => {
  it('removes status-included class', () => {
    const input = '<div class="policy-card status-included">';
    expect(stripStatusMarkersFromContent(input)).toBe('<div class="policy-card">');
  });

  it('removes proposal class', () => {
    const input = '<div class="policy-card proposal">';
    expect(stripStatusMarkersFromContent(input)).toBe('<div class="policy-card">');
  });

  it('removes rule-badge spans', () => {
    const input = '<span class="rule-badge">Included</span>\n<p>Text</p>';
    expect(stripStatusMarkersFromContent(input)).toBe('<p>Text</p>');
  });

  it('removes rule-status divs', () => {
    const input = '<div class="rule-status">Some status</div>\n<p>Text</p>';
    expect(stripStatusMarkersFromContent(input)).toBe('<p>Text</p>');
  });

  it('leaves clean cards unchanged', () => {
    const input = '<div class="policy-card"><p class="rule-stmt">Text</p></div>';
    expect(stripStatusMarkersFromContent(input)).toBe(input);
  });

  it('is idempotent', () => {
    const input = '<div class="policy-card status-included"><span class="rule-badge">X</span></div>';
    const once = stripStatusMarkersFromContent(input);
    expect(stripStatusMarkersFromContent(once)).toBe(once);
  });
});
