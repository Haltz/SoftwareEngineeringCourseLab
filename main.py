from tornado import web, ioloop, httpserver
import json, urllib3
import random
import time, timeit
import os
from src.account import account
from src.account import info as infopy
from src.quiz import make

state = 0  # 记录登录状态
now_user_name = ''  # 现在的用户名
tmp = 0


# 定义视图处理函数
# 主页（选择哪种页面或者登录注册？）
class IndexHandler(web.RequestHandler):
    # 重写get处理方式
    def get(self, *args, **kwargs):
        # 想客户端发送一个数据
        self.render("index.html")

    def post(self):
        pass


# 登录和注册数据怎么区分？
class LoginHandler(web.RequestHandler):

    def get(self, *args, **kwargs):
        # 想客户端发送一个数据
        self.render("login.html", ret='ret')

    def post(self, *args, **kwargs):
        '''
        此函数用来接受登录的post请求
        参数有：
            task: str，表示请求的任务类型，值为 login 或者 signup
            name: str，表示登录或者注册的用户名
            password: str，表示登录或者注册的密码
            email: str，(此项仅仅用于注册)，表示注册的邮箱
            repeat_passwd: str，(此项仅仅用于注册)，表示注册的确认密码
        应该返回：
            dict类型，key应包含'result':str，值应为"success"或者其他字符串和None
        '''
        task = self.get_argument('task')
        if (task == "login"):
            name = self.get_argument("name")
            passwd = self.get_argument("password")
            print(name, passwd, task)
            if (account.login(name, passwd)):
                self.write({"result": "success"})
                return
            else:
                self.write({"result": "failure"})
                return
        if (task == "signup"):
            name = self.get_argument("name")
            passwd = self.get_argument("password")
            email = self.get_argument("email")
            rep_passwd = self.get_argument("repeat_passwd")
            if (rep_passwd != passwd):
                self.write({"result": "failure"})
                return
            if (account.signup(name, email, passwd)):
                self.write({"result": "success"})
                return
            else:
                self.write({"result": "failure"})
                return


class QuestionanswerHandler(web.RequestHandler):
    def get(self):
        self.render("questionanswer.html", sk='sk', result='result')

    def post(self):
        '''
        此函数用来接受请求测试题目和请求测试结果的post请求
        参数有：
            task: str，表示请求的任务类型，值为 request_question 或者 request_result
            number: str，（仅仅用于request_question）表示请求的题目数量
            grade: str，（仅仅用于request_question）值为 "一年级" 或者 "二年级" 或者 "三年级"
            difficulty: str，（仅仅用于request_question）值为 "简单" 或者 "中等" 或者 "困难"
            mode: str 值为 （仅仅用于request_question）"错题重做" 或者 "普通测试"
            username: str，表示用户名
        应该返回：
            如果task == request_question 应当返回
                dict类型，key 应当为 题目的ID， 值应当为题目的 字符串格式
            如果task == request_result 应当返回
                dict类型，key 应当为 字符串类型的错题ID， 值应当为 一个dict类型
                key应当为各项指标的字符串，value应当为指标值的字符串
                #todo 可以有多项指标，都可以显示，有后端指定
        '''
        task = self.get_argument('task')
        if (task == "request_question"):
            username = self.get_argument("username")
            mode = self.get_argument("mode")
            difficulty = self.get_argument("difficulty")
            grade = self.get_argument("grade")
            number = self.get_argument("number")
            if (mode == "normal" or mode == "review"):
                questions = make.makesuitques(grade, eval(number), difficulty)
                dinfo = {str(index): {"ac": questions[index]["cutnum"], "body": questions[index]["show_string"]}
                         for index in questions.keys()}
                dinfo["number"] = number
                dinfo["grade"] = str(grade)
                dinfo["type"] = str(mode)
                dinfo["difficulty"] = str(difficulty)
                tests = infopy.get_tests(username)
                dinfo["id"] = tests["number"] + 1
                json.dump(
                    dinfo,
                    open("data/account/{}/tmp.json".format(username), 'w', encoding='utf-8'))
                self.write({str(index): questions[index]["show_string"] for index in questions.keys()})

        if (task == "request_result"):
            errors = 0
            username = self.get_argument("username")
            info = json.load(open("data/account/{}/tmp.json".format(username), 'r', encoding='utf-8'))
            number = eval(info["number"])
            save = {}
            for i in range(number):
                ans = self.get_argument(str(i))
                tr = info[str(i)]["ac"]
                if (str(ans) != str(tr)):
                    errors += 1
                    save[info[str(i)]["body"]] = {
                        "id": str(i),
                        "wa": str(ans),
                        "ac": str(tr),
                        "grade": info["grade"],
                        "type": info["type"],
                        "difficulty": info["difficulty"]
                    }
            acc = int((1 - errors / number) * 100 + 0.5)
            rate = ""
            if (acc >= 90):
                rate = "A"
            elif (acc >= 80):
                rate = "B"
            elif (acc >= 60):
                rate = "C"
            else:
                rate = "D"

            result = {'errors': errors, 'accuracy': str(acc) + "%", 'level': rate}
            infopy.save_wrongs(username, save)
            test = {
                "grade": info["grade"],
                "type": info["type"],
                "difficulty": info["difficulty"],
                "number": info["number"],
                "wrongs": errors,
                "accuracy": acc,
                "level": rate
            }
            infopy.save_tests(username, test)
            # 返回结果
            self.write(result)


class QuestionsettingHandler(web.RequestHandler):
    '''
    此类用来显示设置题目的页面
    '''

    def get(self):
        self.render('questionsetting.html')

    def post(self):
        pass


# 休闲页面
class RelaxHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("relax.html")

    def post(self):
        '''
        此函数用来接受请求测试题目和请求测试结果的post请求
        参数有：
            task: str，表示请求的任务类型，值为 story 或者 joke 或者 twist
        应该返回：
            dict类型，key 应当为 "text-content"， 值应当为 一段文本
        '''
        pass


# 复习页面（做题记录和错题列表）
class ReviewHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("review.html")

    def post(self):
        '''
        此函数用来接受请求错题记录
        参数有：
            username: str 用户名
        应该返回：
            dict类型，key 应当为 字符串类型的错题ID， 值应当为 一个dict类型
                值的dict应该如下
                {
                    test_type: str 表示测试类型
                    test_grade: str 表示错题的年级
                    test_body: str 表示错题的字符串格式
                    wrong_answer: str 表示答错的答案
                    right_answer: str 表示答正确的答案
                }
        '''
        username = self.get_argument("username")
        wrongs = infopy.get_wrongs(username)
        ret = {}
        for key in wrongs.keys():
            if (key == "number"):
                continue
            ret[key] = {
                "test_type": wrongs[key]["type"],
                "test_grade": wrongs[key]["grade"],
                "test_difficulty": wrongs[key]["difficulty"],
                "test_body": key,
                "wrong_answer": wrongs[key]["wa"],
                "right_answer": wrongs[key]["ac"]
            }
        self.write(ret)


# 个人主页   账户（ID，昵称，年级未显示？，做题记录）
class PersonHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("person.html", info='info')
        # 从数据库获取当前用户信息
        # 反馈给前端

    def post(self):
        '''
        此函数用来接受请求错题记录
        参数有：
            task: str 值应当为 "personinfo" 或者 "testsinfo"
            username: str，表示用户名
        应该返回：
        如果task == "personinfo"
            dict类型，key 应当为 字符串类型， 值应当为 字符串类型
                值的dict应该如下
                {
                    username: str 表示用户名
                    email: str 表示邮箱
                }
        如果task == "testsinfo"
            dict类型，key应当为 测试的ID的字符串，值应当为 一个dict类型
                值的dict应该如下
                {
                    user_name:str 用户名
                    test_id: str 表示测试的ID
                    test_limit_time: str 表示测试限制的时间
                    test_difficulty: str 表示测试的难度
                    test_usetime: str 表示测试使用的时间
                    test_number: str 表示测试题目的数量
                    test_wrong_number: str 表示答错题目的数量
                    test_accuracy: str 表示测试的正确率
                    test.test_level: str 表示测试的评级
                }
        '''
        if self.get_argument('task') == 'personinfo':
            username = self.get_argument("username")
            user = infopy.get_account(username)
            if (user["email"] == ""):
                user['email'] = "You don't write it when sign up."
            self.write({
                "identification": user["id"],
                "username": user["username"],
                "email": user["email"]
            })
        elif self.get_argument('task') == 'testsinfo':
            username = self.get_argument("username")
            tests = infopy.get_tests(username)
            ret = {}
            for key in tests.keys():
                if (key == "number"):
                    continue
                ret[key] = {
                    "username": username,
                    "test_id": key,
                    "test_difficulty": tests[key]["difficulty"],
                    "test_number": tests[key]["number"],
                    "test_wrong_number": tests[key]["wrongs"],
                    "test_accuracy": tests[key]["accuracy"],
                    "test_level": tests[key]["level"],
                }
            self.write(ret)


settings = {
    'template_path': 'templates', 'static_path': 'static', 'static_url_prefix': '/static/', }
# 设置路由
application = web.Application([
    (r'/index', IndexHandler),
    (r'/login', LoginHandler),
    (r'/person', PersonHandler),
    (r'/questionanswer', QuestionanswerHandler),
    (r'/relax', RelaxHandler),
    (r'/review', ReviewHandler),
    (r'/questionsetting', QuestionsettingHandler),
], **settings
)

if __name__ == '__main__':
    #
    ## 创建表
    # con = pymysql.connect("127.0.0.1", "root", "lxt123", charset='utf8')

    # cur = con.cursor()
    ## 开始建库
    ## cur.execute("create database awesome character set utf8;")
    ## 使用库
    # cur.execute('use awesome;')
    ## 建表
    # cur.execute('''
    #     CREATE TABLE INFOM(id int unsigned primary key auto_increment not null,
    #     user_name CHAR(20) NOT NULL,passw CHAR(20))
    #    ''')
    # cur.close()
    # con.close()
    http_server = httpserver.HTTPServer(application)
    http_server.listen(8080)
    ioloop.IOLoop.current().start()
