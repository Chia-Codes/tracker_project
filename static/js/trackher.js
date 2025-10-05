(function () {
  const selectedDates = new Set();
  const $selected = document.getElementById("selected-date");
  const $form = document.getElementById("cycle-log-form");
  const $single = document.getElementById("id_date");
  const $multiWrap = document.getElementById("multi-date-container");
  const $multiToggle = document.getElementById("multi-select");

  function fmt(d) {
    return d;
  }
  function renderSelected() {
    if (!$selected) return;
    if (selectedDates.size === 0) {
      $selected.textContent = "No date selected.";
      return;
    }
    const arr = Array.from(selectedDates).sort();
    $selected.textContent =
      (arr.length === 1 ? "Selected: " : "Selected (" + arr.length + "): ") +
      arr.join(", ");
  }
  function syncInputs() {
    if (!$form) return;
    // clear prior multi inputs
    if ($multiWrap) $multiWrap.innerHTML = "";
    if ($multiToggle && $multiToggle.checked && selectedDates.size > 1) {
      $single && ($single.value = "");
      Array.from(selectedDates).forEach((d) => {
        const i = document.createElement("input");
        i.type = "hidden";
        i.name = "dates";
        i.value = d; // Django: request.POST.getlist('dates')
        $multiWrap.appendChild(i);
      });
    } else {
      // single date mode
      const only = selectedDates.values().next().value || "";
      if ($single) $single.value = only;
    }
  }
  function toggleCell(el) {
    const d = el.getAttribute("data-date");
    if (!d) return;
    const multi = $multiToggle && $multiToggle.checked;
    if (!multi) {
      selectedDates.clear();
    }
    if (selectedDates.has(d) && multi) {
      selectedDates.delete(d);
      el.classList.remove("selected");
    } else {
      selectedDates.add(d);
      el.classList.add("selected");
    }
    // if single mode, also clear other .selected classes
    if (!multi) {
      document.querySelectorAll(".calendar-day.selected").forEach((c) => {
        if (c !== el) c.classList.remove("selected");
      });
    }
    renderSelected();
    syncInputs();
  }
  // Bind clicks
  document.addEventListener("click", function (ev) {
    const cell = ev.target.closest(".calendar-day");
    if (cell) toggleCell(cell);
    // Flow quick buttons
    const flowBtn = ev.target.closest(".flow-btn[data-flow]");
    if (flowBtn) {
      const flowVal = flowBtn.getAttribute("data-flow");
      const flowInput = document.getElementById("id_flow");
      if (flowInput) {
        flowInput.value = flowVal;
        flowInput.dispatchEvent(new Event("change"));
      }
      // Optional: auto-scroll to form
      if ($form) $form.scrollIntoView({ behavior: "smooth", block: "start" });
    }
  });
})();
