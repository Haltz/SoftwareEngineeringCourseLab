function checklogin() {
    if ($.cookie('username') == null) {
        alert("Please login first.");
        window.location.href = "/login";
    }
}

$(document).ready(checklogin());

function story() {
    $.ajax({
        url: "/relax",
        type: "POST",
        data: {
            task: "story"
        },
        dataType: "json",
        success: function (response) {
            document.getElementById("text-content").innerHTML = response;
        }
    })
}

function joke() {
    $.ajax({
        url: "/relax",
        type: "POST",
        data: {
            task: "joke"
        },
        dataType: "json",
        success: function (response) {
            document.getElementById("text-content").innerHTML = response;
        }
    })
}

function twist() {
    $.ajax({
        url: "/relax",
        type: "POST",
        data: {
            task: "twist"
        },
        dataType: "json",
        success: function (response) {
            document.getElementById("text-content").innerHTML = response;
        }
    })
}