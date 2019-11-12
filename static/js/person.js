$(document).ready(function () {
    if($.cookie("username") == null){
        alert("Please login first!");
        window.location.href = "/login";
    }
    var username = $.cookie("username");
    // alert(username);
    $.ajax({
        type: "POST",
        url: "/person",
        data: {
            task: "personinfo",
            username: username
        },
        dataType: "json",
        success: function (response) {
            document.getElementById('identification').innerHTML = response.identification;
            document.getElementById('username').innerHTML = response.username;
            document.getElementById('email').innerHTML = response.email;
        }
    });

    $.ajax({
        type: "POST",
        url: "/person",
        data: {
            task: "testsinfo",
            username: username
        },
        dataType: "json",
        success: function (response) {
            var testsinfo = "";
            for (var testid in response) {
                test = response[testid];
                testsinfo += "<tr>\n" +
                    "\t\t\t\t\t\t\t<th>" + test.test_id + "</th>\n" +
                    "\t\t\t\t\t\t\t<td>" + test.test_limit_time + "</td>\n" +
                    "\t\t\t\t\t\t\t<td>" + test.test_difficulty + "</td>\n" +
                    "\t\t\t\t\t\t\t<td>" + test.test_usetime + "</td>\n" +
                    "\t\t\t\t\t\t\t<td>" + test.test_number + "</td>\n" +
                    "\t\t\t\t\t\t\t<td>" + test.test_wrong_number + "</td>\n" +
                    "\t\t\t\t\t\t\t<td>" + test.test_accuracy + "</td>\n" +
                    "\t\t\t\t\t\t\t<td>" + test.test_level + "</td>\n" +
                    "\t\t\t\t\t\t</tr>"
            }
            document.getElementById('testsinfo').innerHTML=testsinfo;
        }
    });
});