
(function () {
  function $(sel, root = document) { return root.querySelector(sel); }
  function $all(sel, root = document) { return Array.from(root.querySelectorAll(sel)); }

  function updateButtons() {
    const checkboxes = $all('.log-checkbox');
    const checkedCount = checkboxes.filter(cb => cb.checked).length;

    const logFlowBtn = $('#log-flow-btn');
    const submitBtn  = $('#submit-log-btn');

    if (logFlowBtn) logFlowBtn.classList.toggle('d-none', checkedCount < 2);
    if (submitBtn)  submitBtn.classList.toggle('d-none',  checkedCount >= 2);
  }

  function onCheckboxChange(e) {
    const cb = e.target;
    if (!(cb instanceof HTMLInputElement)) return;

    const cell = cb.closest('td');
    if (cell) cell.classList.toggle('selected-date', cb.checked);

    updateButtons();
  }

  function initTrackHer() {
    const checkboxes = $all('.log-checkbox');
    if (checkboxes.length === 0) return;

    checkboxes.forEach(cb => cb.addEventListener('change', onCheckboxChange));

    // reflect any pre-checked boxes on page load
    checkboxes.forEach(cb => {
      const cell = cb.closest('td');
      if (cell) cell.classList.toggle('selected-date', cb.checked);
    });

    updateButtons();
  }

  // Run in browser
  if (typeof document !== 'undefined') {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', initTrackHer);
    } else {
      initTrackHer();
    }
  }

  // Export for Jest
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { __initTrackHer: initTrackHer };
  }
})();


