$(document).ready(
    function () {
        var useragent = navigator.userAgent;
        if (useragent.match(/AppleWebKit/i) != "AppleWebKit") {
            alert("You should visit this website using GOOGLE GHROME!!!\n Visit is stopped!!!");
            window.location.href = "/";
        }
    }
);