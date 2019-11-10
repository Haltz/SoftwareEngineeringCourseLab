function checklogin() {
    if ($.cookie('username') == null) {
        alert("Please login first.");
        window.location.href = "/login";
    }
}

$(document).ready(checklogin());

$.ajax({
    url: "/review",
    type: "POST",
    data: {
        username: $.cookie('username')
    },
    dataType: "json",
    success: function (response) {
        document.getElementById("wrong_questions_body").innerHTML = "";
        for (var id in response) {
            var info = "";
            var test = response.id;
            info = "<tr>\n" +
                "                    <th>" + id + "</th>\n" +
                "                    <td>" + test.test_type + "</td>\n" +
                "                    <td>" + test.test_grade + "</td>\n" +
                "                    <td>" + test.test_body + "</td>\n" +
                "                    <td>" + test.wrong_answer + "</td>\n" +
                "                    <td>" + test.right_answer + "</td>\n" +
                "                </tr>"
            document.getElementById("wrong_questions_body").innerHTML += info;
        }
    }
})