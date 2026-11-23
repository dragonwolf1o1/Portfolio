/* Portfolio interactions — vanilla JS, no dependencies. */
(function () {
  "use strict";
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  /* ---- Mobile menu (replaces the old hamburger) ---- */
  var btn = $("#menu-btn"), menu = $("#mobile-menu");
  function setMenu(open) {
    if (!btn || !menu) return;
    menu.classList.toggle("hidden", !open);
    btn.setAttribute("aria-expanded", String(open));
    btn.setAttribute("aria-label", open ? "Close navigation" : "Open navigation");
    $("[data-icon-open]", btn).classList.toggle("hidden", open);
    $("[data-icon-close]", btn).classList.toggle("hidden", !open);
  }
  if (btn && menu) {
    btn.addEventListener("click", function () { setMenu(btn.getAttribute("aria-expanded") !== "true"); });
    $$("a", menu).forEach(function (a) { a.addEventListener("click", function () { setMenu(false); }); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") setMenu(false); });
    window.matchMedia("(min-width: 768px)").addEventListener("change", function (e) { if (e.matches) setMenu(false); });
  }

  /* ---- Avatar fallback (initials) if the remote image fails ---- */
  $$("img[data-avatar]").forEach(function (img) {
    function fail() { img.remove(); }
    if (img.complete && img.naturalWidth === 0 && img.currentSrc) fail();
    img.addEventListener("error", fail);
  });

  /* ---- Scroll-spy for the nav ---- */
  var sections = $$("[data-section]");
  var links = $$(".nav-link, #mobile-menu a");
  function activate(key) {
    links.forEach(function (a) {
      if (a.getAttribute("data-nav") === key) a.setAttribute("aria-current", "true");
      else a.removeAttribute("aria-current");
    });
  }
  if ("IntersectionObserver" in window && sections.length) {
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) activate(en.target.getAttribute("data-nav")); });
    }, { rootMargin: "-45% 0px -50% 0px" });
    sections.forEach(function (s) { spy.observe(s); });
    var top = $("#top");
    if (top) new IntersectionObserver(function (e) { if (e[0].isIntersecting) activate(""); }, { rootMargin: "-45% 0px -50% 0px" }).observe(top);
  }

  /* ---- Scroll reveal ---- */
  var reveals = $$(".reveal");
  if ("IntersectionObserver" in window && !reduce) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); } });
    }, { threshold: 0.08, rootMargin: "0px 0px -40px 0px" });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("in"); });
  }

  /* ---- Hero metric count-up ---- */
  $$("[data-count]").forEach(function (el) {
    var target = parseFloat(el.getAttribute("data-count")), suffix = el.getAttribute("data-suffix") || "";
    if (reduce || isNaN(target)) return;
    var done = false;
    function run() {
      if (done) return; done = true;
      var t0 = null, dur = 1100;
      el.textContent = "0" + suffix;
      requestAnimationFrame(function step(ts) {
        if (t0 === null) t0 = ts;
        var p = Math.min((ts - t0) / dur, 1), eased = 1 - Math.pow(1 - p, 3);
        el.textContent = Math.round(target * eased) + suffix;
        if (p < 1) requestAnimationFrame(step); else el.textContent = target + suffix;
      });
    }
    if ("IntersectionObserver" in window) {
      var o = new IntersectionObserver(function (e) { if (e[0].isIntersecting) { run(); o.disconnect(); } });
      o.observe(el);
    } else run();
  });

  /* ---- Skill bars animate when scrolled into view ---- */
  var fills = $$(".skill-fill");
  if ("IntersectionObserver" in window && !reduce && fills.length) {
    fills.forEach(function (f) { f.style.width = "0%"; });
    var so = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.style.width = en.target.getAttribute("data-width") + "%"; so.unobserve(en.target); }
      });
    }, { threshold: 0.3 });
    fills.forEach(function (f) { so.observe(f); });
  }

  /* ---- Copy email ---- */
  var copyBtn = $("#copy-email-btn"), copyLabel = $("#copy-email-label");
  if (copyBtn && copyLabel) {
    copyBtn.addEventListener("click", function () {
      var email = copyBtn.getAttribute("data-email");
      function ok() { copyLabel.textContent = "Copied"; setTimeout(function () { copyLabel.textContent = "Copy"; }, 2000); }
      if (navigator.clipboard && window.isSecureContext) {
        navigator.clipboard.writeText(email).then(ok, fallback);
      } else fallback();
      function fallback() {
        var ta = document.createElement("textarea");
        ta.value = email; ta.setAttribute("readonly", ""); ta.style.position = "fixed"; ta.style.opacity = "0";
        document.body.appendChild(ta); ta.select();
        try { if (document.execCommand("copy")) ok(); } catch (e) { /* ignore */ }
        document.body.removeChild(ta);
      }
    });
  }
})();
