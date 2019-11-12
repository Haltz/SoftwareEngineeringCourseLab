var url = location.search;
var urlparam = {};
if (url.indexOf('?') != -1) {
    // ?grade=  &difficulty=  &mode=
    url = url.substr(1);
    param = url.split('&');
    for (var i = 0; i < param.length; i++) {
        urlparam[param[i].split('=')[0]] = param[i].split('=')[1];
    }
    urlparam.task = "request_question";
    $.ajax({
        type: "POST",
        url: "/questionanswer",
        data: urlparam,
        dataType: "json",
        success: function (response) {

            for (var item in response) {
                document.getElementById("questions").innerHTML = '<div><a class="" href="#">' + response[item] + '</a><a>答案:<input type="text" name="answer" style="width: 50px; background-color: inherit; border: 0"></a></div>' + document.getElementById("questions").innerHTML;
            }
        }
    });
} else {
    window.location.href = '/questionsetting';
}

function alldone() {
    document.getElementById("submit_answers").innerHTML = "";
    var ret = document.getElementsByTagName("input");
    var answers = new Object();
    for (var i = 0; i < ret.length; i++) {
        var s = String(i);
        if(ret[i].value == ""){
            answers[s]="999999999";
        }
        else {answers[s] = ret[i].value;}
    }

    answers.task = "request_result";
    $.ajax({
        type: "POST",
        url: "/questionanswer",
        data: answers,
        dataType: "json",
        success: function (response) {
            document.getElementById("questions").innerHTML = "";
            for (var item in response) {
                var info = "";
                info += item;
                info += " = " + response[item] + "\n";
                alert(info);
                document.getElementById("questions").innerHTML += '<div>\n' +
                    '\t\t\t\t\t\t\t\t<a class="" href="#">' + info + '</a>\n' +
                    '\t\t\t\t\t\t\t</div>'
            }
        }
    });
}