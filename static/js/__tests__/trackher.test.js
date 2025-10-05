/**
 * @file static/js/__tests__/trackher.test.js
 * JSDOM tests that simulate user clicks on the calendar checkboxes
 * and assert the Log Flow / Submit Log buttons toggle visibility,
 * and selected dates get a CSS marker class.
 */

describe('TrackHer calendar interactions', () => {
  // Build a minimal DOM that mirrors your template structure
  const html = `
    <div>
      <a id="submit-log-btn" class="btn btn-primary">Submit Log</a>
      <button id="log-flow-btn" class="btn btn-danger d-none">Log Flow</button>
      <table class="table"><tbody>
        <tr>
          <td class="cell"><input type="checkbox" class="log-checkbox" value="2025-10-01"></td>
          <td class="cell"><input type="checkbox" class="log-checkbox" value="2025-10-02"></td>
          <td class="cell"><input type="checkbox" class="log-checkbox" value="2025-10-03"></td>
        </tr>
      </tbody></table>
    </div>
  `;

  /** lazy-load module under JSDOM */
  async function loadScript() {
    // Put DOM into document
    document.body.innerHTML = html;

    // Load script from static path relative to the test file
    const mod = require('../trackher.js');

    // dispatch DOMContentLoaded to trigger listeners
    if (mod && typeof mod.__initTrackHer === 'function') {
      mod.__initTrackHer();
    } else {
      document.dispatchEvent(new Event('DOMContentLoaded'));
    }
  }

  function q(sel) { return document.querySelector(sel); }
  function qa(sel) { return Array.from(document.querySelectorAll(sel)); }

  test('Log Flow stays hidden until 2+ days selected', async () => {
    await loadScript();

    const logFlow = q('#log-flow-btn');
    const submit = q('#submit-log-btn');
    const cbs = qa('.log-checkbox');

    // initially: 0 selected → Log Flow hidden, Submit visible
    expect(logFlow.classList.contains('d-none')).toBe(true);
    expect(submit.classList.contains('d-none')).toBe(false);

    // select one
    cbs[0].checked = true;
    cbs[0].dispatchEvent(new Event('change', { bubbles: true }));

    expect(logFlow.classList.contains('d-none')).toBe(true);
    expect(submit.classList.contains('d-none')).toBe(false);

    // select another (now 2 total)
    cbs[1].checked = true;
    cbs[1].dispatchEvent(new Event('change', { bubbles: true }));

    expect(logFlow.classList.contains('d-none')).toBe(false); 
    expect(submit.classList.contains('d-none')).toBe(true);    
  });

  test('Selected dates get .selected-date on the <td> cell', async () => {
    await loadScript();
    const cbs = qa('.log-checkbox');

    const parentCell = cb => cb.closest('td');

    // toggle first checkbox → parent td gets selected-date
    cbs[0].checked = true;
    cbs[0].dispatchEvent(new Event('change', { bubbles: true }));
    expect(parentCell(cbs[0]).classList.contains('selected-date')).toBe(true);

    // uncheck → class removed
    cbs[0].checked = false;
    cbs[0].dispatchEvent(new Event('change', { bubbles: true }));
    expect(parentCell(cbs[0]).classList.contains('selected-date')).toBe(false);
  });
});