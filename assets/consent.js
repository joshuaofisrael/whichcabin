(function () {
  var KEY = "whichcabin-consent";
  var banner = document.getElementById("consent-banner");
  var loader = document.getElementById("ga4-loader");
  var ga4 = loader ? (loader.getAttribute("data-ga4-id") || "") : "";
  var src = loader ? (loader.getAttribute("data-src") || "") : "";

  function gtag() {
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push(arguments);
  }
  if (!window.gtag) window.gtag = gtag;

  function callGtag() {
    window.gtag.apply(window, arguments);
  }
  function remember(value) {
    try { localStorage.setItem(KEY, value); } catch (e) {}
  }
  function stored() {
    try { return localStorage.getItem(KEY); } catch (e) { return null; }
  }
  function validId(id) {
    return /^G-[A-Z0-9]+$/.test(id);
  }
  function loadGa() {
    if (!validId(ga4) || !src || src.indexOf(ga4) === -1 || window.__whichcabinGa4) return;
    window.__whichcabinGa4 = true;
    callGtag("consent", "update", {
      analytics_storage: "granted",
      ad_storage: "denied",
      ad_user_data: "denied",
      ad_personalization: "denied"
    });
    var s = document.createElement("script");
    s.async = true;
    s.src = src;
    document.head.appendChild(s);
    callGtag("js", new Date());
    callGtag("config", ga4);
  }
  function deny() {
    callGtag("consent", "update", {
      analytics_storage: "denied",
      ad_storage: "denied",
      ad_user_data: "denied",
      ad_personalization: "denied"
    });
  }
  function openBanner(focus) {
    if (!banner) return;
    banner.hidden = false;
    if (focus) {
      var btn = document.getElementById("consent-accept");
      if (btn) btn.focus();
    }
  }
  function closeBanner() {
    if (banner) banner.hidden = true;
  }
  function choose(value) {
    remember(value);
    closeBanner();
    if (value === "accepted") loadGa();
    else deny();
  }
  if (banner) {
    var accept = document.getElementById("consent-accept");
    var reject = document.getElementById("consent-reject");
    if (accept) accept.addEventListener("click", function () { choose("accepted"); });
    if (reject) reject.addEventListener("click", function () { choose("rejected"); });
  }
  document.addEventListener("click", function (e) {
    var t = e.target;
    if (!t || !t.closest) return;
    if (t.closest("#cookie-settings")) {
      e.preventDefault();
      openBanner(true);
    }
  });
  var choice = stored();
  if (choice === "accepted") loadGa();
  else if (choice !== "rejected") openBanner(false);
})();
