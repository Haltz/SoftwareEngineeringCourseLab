$(document).ready(function () {
    //$('#username').focus();

    $('#submit').click(function () {

        event.preventDefault(); // prevent PageReLoad

        var ValidEmail = $('#username').val() === 'invitado'; // User validate
        var ValidPassword = $('#password').val() === 'hgm2015'; // Password validate

        if (ValidEmail === true && ValidPassword === true) { // if ValidEmail & ValidPassword
            $('.valid').css('display', 'block');
            window.location = "http://arkev.com"; // go to home.html
        } else {
            $('.error').css('display', 'block'); // show error msg
        }
    });
});

function login(param) {
    alert("login");
    var name = param["name"];
    var email = param["email"];
    var password = param["password"];
    $.ajax({
        type: "POST",
        url: "",
        data: {
            name: name,
            email: email,
            password: password
        },
        dataType: "json",
        success: function (response) {
            if (response == "success") {
                alert("login success");
            }
        }
    });
}
location.href = 1;

function signup(param) {
    alert("signup");
    var name = param["name"];
    var email = param["email"];
    var password = param["password"];
    $.ajax({
        type: "POST",
        url: "",
        data: {
            name: name,
            email: email,
            password: password
        },
        dataType: "json",
        success: function (response) {
            if (response == "success") {
                alert("signup success");
            }
        }
    })
}

function setcookie (name, value) {
    
  }