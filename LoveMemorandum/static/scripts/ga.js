function insert(i, s, o, g, r, a, m, k) {
    i["GoogleAnalyticsObject"] = r;
    i[r] = i[r] || function() {
        (i[r].q = i[r].q || []).push(arguments);
    }, i[r].l = 1 * new Date();
    a = s.createElement(o), m = s.getElementsByTagName(o)[0];
    a.async = 1;
    a.src = g;
    m.parentNode.insertBefore(a, m);
}

insert(window, document, "script", "https://www.google-analytics.com/analytics.js", "ga", 1);

insert(window, document, "script", "https://webapi.amap.com/maps?v=1.3&key=f9c83cfb12c018f512d8a97878b8c580&plugin=AMap.Driving,AMap.Transfer,AMap.Walking,AMap.PlaceSearch,AMap.Geocoder", "ga", 0);

ga("create", "UA-7969851-10", "auto");

ga("send", "pageview");

var GaodeKey = "e5035e84785eb4da3362836ee5f92cf8", DisplayKey = "f9c83cfb12c018f512d8a97878b8c580";