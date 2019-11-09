$(document).ready(function () {
    alert("what the fuck?");
});

function login(param) {
    var username = param.username;
    var password = param.password;
    $.ajax({
        type: "POST",
        url: "/login",
        data: {
            name: username,
            password: password
        },
        dataType: "json",
        success: function (response) {
            console.log(response);
        }
    });
}

// location.href = 1;

function signup(param) {
    var name = param.username;
    var email = param.email;
    var passwd = param.password;
    var repeat_passwd = param.repeat_password;
    $.ajax({
        type: "POST",
        url: "",
        data: {
            name: name,
            email: email,
            password: passwd,
            repeat_passwd: repeat_passwd
        },
        dataType: "json",
        success: function (response) {
            if (response.result == "success") {
                alert("signup success");
            }
        }
    })
}

//
// function keeplogin() {
//     name
// }



