var earthLatLon, map, t, marsLonLat,
    nearestStation = [],
    currentCity = $("#CurrentCity").text();

function showLocation(position) {
    eWJ = [position.coords.latitude, position.coords.longitude];
    $("#location").val(eWJ[0] + "," + eWJ[1]);
}


function displayAddress(latlng) {
    if (!(latlng.hasClass("address"))) {
        $.get('https://ditu.google.cn/maps/api/geocode/json', {
            latlng: latlng.text(),
            language: 'zh-CN'
        }, function(data) {
            if (data["status"] === "OK") {
                last = data["results"].length - 1;
                if (data["results"][last]["formatted_address"] === "中国") {
                    toMars(latlng.text().split(","), latlng);
                } else {
                    latlng.html($("<a>", {
                        href: 'https://www.google.cn/maps/place/' + latlng.text()
                    }).html(data["results"][0]["formatted_address"]));
                }
                latlng.addClass("address");
            }
        });
    }
}

function getAddresses() {
    $('span#location').each(function() {
        displayAddress($(this));
    });
}


function toMars(eWJ, p) {
    url = "https://restapi.amap.com/v3/assistant/coordinate/convert";
    $.get(url, {
        key: GaodeKey,
        locations: eWJ[1] + "," + eWJ[0],
        coordsys: "gps"
    }, function(data) {
        marsLonLat = data["locations"].split(",");
        var placeSearch = new AMap.Geocoder();
        placeSearch.getAddress(data["locations"], function(status, result) {
            p.html($("<a>", {
                href: "http://m.amap.com/navi/?dest=" + data["locations"] + "&destName=%E8%BF%99%E9%87%8C&hideRouteIcon=1&key=" + DisplayKey
            }).html(result["regeocode"]["formattedAddress"]));
        });
    });
}

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showLocation, showError);
    } else {
        alert("您的浏览器不支持定位。");
    }
}

function showError(error) {
    switch (error.code) {
        case error.PERMISSION_DENIED:
            alert("您拒绝提供位置信息，因此我们无法为您定位。");
            break;
        case error.POSITION_UNAVAILABLE:
            alert("我们不知道您在哪儿。");
            break;
        case error.TIMEOUT:
            alert("暂时无法获得位置信息。");
            break;
        case error.UNKNOWN_ERROR:
            alert("发生了无法处理的意外事件。");
            break;
    }
}

function resize() {
    a = $("#navbarcontainer").height() + 20;
    $("body").attr("style", "padding-top: " + a + "px");
}
$(window).resize(resize);
$(function() {
    resize();
    getLocation();
});