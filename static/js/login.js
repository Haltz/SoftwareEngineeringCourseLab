function login(param) {
    var username = param.username;
    var password = param.password;
    $.ajax({
        type: "POST",
        url: "/login",
        data: {
            task: "login",
            name: username,
            password: password
        },
        dataType: "json",
        success: function (response) {
            if (response.result == "success") {
                alert("Login Success!");
                $.cookie('username', username, {path: '/', expires: 30});
                window.location.href = '/index';
            }
            else {
                alert('Login failed. Please login again.');
                window.location.href = '/login';
            }
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
        url: "/login",
        data: {
            task: "signup",
            name: name,
            email: email,
            password: passwd,
            repeat_passwd: repeat_passwd
        },
        dataType: "json",
        success: function (response) {
            if (response.result == "success") {
                alert("Signup Success!");
                window.location.href = '/login';
            } else {
                alert("Signup failed. It means your username has been taken. You should consider a better nickname.");
                window.location.href = '/login';
            }
        }
    })
}




