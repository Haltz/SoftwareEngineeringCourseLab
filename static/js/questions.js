var url = location.search;
var urlparam = {};
if (url.indexOf('?') != -1) {
    // ?grade=  &difficulty=  &mode=
    url = url.substr(1);
    param = url.split('&');
    for (var i = 0; i < param.length; i++) {
        urlparam[param[i].split('=')[0]] = param[i].split('=')[1];
    }
    $.ajax({
        type: "POST",
        url: "",
        data: urlparam,
        dataType: "json",
        success: function (response) {
            for (var item in response) {
                document.getElementById("questions").innerHTML += '<div><a class="" href="#">' + item + '</a><a>答案:<input type="text" name="answer" style="width: 50px; background-color: inherit; border: 0"></a></div>';
            }
        }
    });
} else {
    window.location.href = 'question_setting.html';
}

function alldone() {
    var ret = document.getElementsByTagName("input");
    var answers = new Object();
    for (var i = 0; i < ret.length; i++) {
        answers[i] = ret[i].value;
    }
    $.ajax({
        type: "POST",
        url: "",
        data: answers,
        dataType: "json",
        success: function (response) {
            var i = 0;
        }
    });
}