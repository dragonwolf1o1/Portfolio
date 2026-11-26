/* Technical Architecture component — vanilla JS, no dependencies.
   Features: ARIA tabs (+ project selector), deep links (#architecture/<tab>[/<project>]),
   diagram lightbox (<dialog>), copy-to-clipboard. Without JS all panels render stacked. */
(function () {
  "use strict";
  var root = document.querySelector("[data-arch]");
  if (!root) return;
  var $ = function (s, r) { return (r || root).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || root).querySelectorAll(s)); };
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  root.classList.add("arch--js");

  var tabs = $$(".arch-tab"), panels = $$(".arch__panel");
  var chips = $$(".arch-chip"), projs = $$(".arch-proj");
  var state = { tab: "model", proj: "credit-risk" };

  /* ---- generic tab wiring ---- */
  function show(list, items, key, attr) {
    list.forEach(function (t) {
      var on = t.getAttribute("data-key") === key;
      t.setAttribute("aria-selected", String(on));
      t.tabIndex = on ? 0 : -1;
    });
    items.forEach(function (p) { p.hidden = p.getAttribute("data-panel") !== key; });
  }
  function render() { show(tabs, panels, state.tab); show(chips, projs, state.proj); }

  function writeHash() {
    var h = "#architecture/" + state.tab + (state.tab === "pipelines" ? "/" + state.proj : "");
    try { history.replaceState(null, "", h); } catch (e) { /* file:// or sandboxed */ }
  }
  function readHash() {
    var m = (location.hash || "").match(/^#architecture\/([\w-]+)(?:\/([\w-]+))?/);
    if (!m) return false;
    if (tabs.some(function (t) { return t.getAttribute("data-key") === m[1]; })) state.tab = m[1];
    if (m[2] && chips.some(function (t) { return t.getAttribute("data-key") === m[2]; })) state.proj = m[2];
    return true;
  }

  function keynav(list, onPick) {
    list.forEach(function (el, i) {
      el.addEventListener("keydown", function (e) {
        var n = null;
        if (e.key === "ArrowRight" || e.key === "ArrowDown") n = (i + 1) % list.length;
        else if (e.key === "ArrowLeft" || e.key === "ArrowUp") n = (i - 1 + list.length) % list.length;
        else if (e.key === "Home") n = 0;
        else if (e.key === "End") n = list.length - 1;
        if (n === null) return;
        e.preventDefault(); list[n].focus(); onPick(list[n]);
      });
    });
  }
  tabs.forEach(function (t) { t.addEventListener("click", function () { pickTab(t); }); });
  chips.forEach(function (t) { t.addEventListener("click", function () { pickProj(t); }); });
  function pickTab(t) { state.tab = t.getAttribute("data-key"); render(); writeHash(); }
  function pickProj(t) { state.proj = t.getAttribute("data-key"); render(); writeHash(); }
  keynav(tabs, pickTab); keynav(chips, pickProj);

  var fromHash = readHash();
  render();
  if (fromHash) {
    /* a deep link means the visitor wants this section on screen */
    root.scrollIntoView({ behavior: "auto", block: "start" });
  }
  window.addEventListener("hashchange", function () { if (readHash()) { render(); } });

  /* ---- lightbox ---- */
  var dlg = $(".arch-lightbox");
  var lastTrigger = null;
  function closeDlg() { if (dlg && dlg.open) dlg.close(); }
  root.addEventListener("click", function (e) {
    var ex = e.target.closest("[data-arch-expand]");
    if (ex && dlg) {
      var fig = ex.closest(".arch-fig");
      var svg = $("svg", fig) || $("img", fig);
      if (!svg) return;
      lastTrigger = ex;
      $(".arch-lightbox__title", dlg).textContent = $(".arch-fig__title", fig).textContent;
      var body = $(".arch-lightbox__body", dlg);
      body.innerHTML = "";
      var clone = svg.cloneNode(true);
      /* unique ids so marker references inside the clone stay valid */
      var ids = {};
      $$("[id]", clone).forEach(function (n) { ids[n.id] = n.id + "-x"; n.id = n.id + "-x"; });
      $$("*", clone).forEach(function (n) {
        Array.prototype.slice.call(n.attributes).forEach(function (a) {
          var v = a.value;
          if (v.indexOf("url(#") !== -1 || a.name === "aria-labelledby") {
            Object.keys(ids).forEach(function (k) { v = v.split(k + ")").join(ids[k] + ")").split(k + " ").join(ids[k] + " "); });
            if (a.name === "aria-labelledby") v = v.split(" ").map(function (s) { return ids[s] || s; }).join(" ");
            n.setAttribute(a.name, v);
          }
        });
      });
      clone.removeAttribute("width"); clone.removeAttribute("height");
      body.appendChild(clone);
      if (typeof dlg.showModal === "function") dlg.showModal(); else dlg.setAttribute("open", "");
      return;
    }
    if (e.target.closest("[data-arch-close]")) { closeDlg(); return; }
    var cp = e.target.closest("[data-arch-copy]");
    if (cp) copy(cp);
  });
  if (dlg) {
    dlg.addEventListener("click", function (e) { if (e.target === dlg) closeDlg(); });   /* backdrop click */
    dlg.addEventListener("close", function () { if (lastTrigger) lastTrigger.focus(); });
  }

  /* ---- copy to clipboard ---- */
  function copy(btn) {
    var code = $("code", btn.parentNode);
    if (!code) return;
    var text = code.textContent;
    function ok() {
      btn.textContent = "Copied"; btn.setAttribute("data-state", "done");
      setTimeout(function () { btn.textContent = "Copy"; btn.removeAttribute("data-state"); }, 1800);
    }
    function fallback() {
      var ta = document.createElement("textarea");
      ta.value = text; ta.setAttribute("readonly", ""); ta.style.cssText = "position:fixed;opacity:0;top:0;left:0";
      document.body.appendChild(ta); ta.select();
      try { if (document.execCommand("copy")) ok(); } catch (err) { /* ignore */ }
      document.body.removeChild(ta);
    }
    if (navigator.clipboard && window.isSecureContext) navigator.clipboard.writeText(text).then(ok, fallback);
    else fallback();
  }

  /* ---- optional: scroll fixed-header offset for in-page links to #architecture ---- */
  if (reduce) root.style.scrollBehavior = "auto";
})();
