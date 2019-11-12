from tornado import web, ioloop, httpserver
import json, urllib3
import time, timeit
import issue
import os
from denglu import *
from zhuce import *

state = 0  # 记录登录状态
now_user_name = ''  # 现在的用户名


# 定义视图处理函数
# 主页（选择哪种页面或者登录注册？）
class IndexHandler(web.RequestHandler):
    # 重写get处理方式
    def get(self, *args, **kwargs):
        # 想客户端发送一个数据
        self.render("index.html")

    #def post(self):
    #    exit = self.get_argument('exit')
    #    if exit == 1:
    #        state = 0
    #        now_user_name = ''


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
            repeat_password: str，(此项仅仅用于注册)，表示注册的确认密码
        应该返回：
            dict类型，key应包含'result':str，值应为"success"或者其他字符串和None
        '''
        task=self.get_argument('task')
        ret = {'result': 'success'}
        # if task=='login':
        #     name=self.get_argument('name')
        #     password=self.get_argument('password')
        #     result=denglu(name,password)
        #     if result==0:
        #         ret = {'result': 'success'}
        #         state = 1
        #         now_user_name = 'name'
        #     else:
        #         ret = {'result': 'fail'}
        # else:
        #     name = self.get_argument('name')
        #     password = self.get_argument('password')
        #     repeat_password = self.get_argument('repeat_password')
        #     email = self.get_argument('email')
        #     if password!=repeat_password:
        #         ret = {"result": "fail"}
        #     else:
        #         result = zhuce(name, password, email)
        #         if result==0:
        #             ret = {'result': 'success'}
        #         else:
        #             ret = {'result': 'fail'}
        self.write(ret)


# # 做题页面
# class QuestionanswerHandler(web.RequestHandler):
#     def get(self, *args, **kwargs):
#         self.render("questionanswer.html", sk='sk')
#         # 传用户选择的设置
#
#     def post(self):
#         chose = json.loads(self.request.body)
#         # 生成题目并传到前端
#         sk = {}
#         ak = {}
#         for i in range(1, chose['number'] + 1):
#             skak = issue.issues(chose['grade'], chose['mode'])
#             sk[i] = skak['sk']
#             ak[i] = skak['ak']
#         self.write(sk)
#         # 开始计时
#         t0 = timeit.default_timer()
#         # 接受答案
#         student_ak = json.loads(self.request.body)
#         # 计时结束
#         # 批改答案
#         error_amount = 0
#         for i in range(1, chose['number'] + 1):
#             if student_ak[i] != ak[i]:
#                 error_amount += 1
#         accuracy = 1 - float(error_amount) / float(chose['number'])
#         if accuracy >= 0.9:
#             rate = 'A'
#         elif accuracy >= 0.8:
#             rate = 'B'
#         elif accuracy >= 0.6:
#             rate = 'C'
#         else:
#             rate = 'D'
#         # 返回结果
#         self.write({'error_amount': error_amount, 'accuracy': accuracy, 'rate': rate})
#     # 数据记录到数据库中


class QuestionanswerHandler(web.RequestHandler):
    def get(self):
        self.render("questionanswer.html", sk='sk',result='result')

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
        # for test
        # if (task == "test"):
        #     self.write({1: '1 X 2 = __'})
        #     return
        sk = {}
        ak = {}
        number=1
        if (task == "request_question"):
            # 生成题目并传到前端
            number=int(self.get_argument('number'))
            grade = self.get_argument('grade')
            difficulty = self.get_argument('difficulty')
            for i in range(1, int(number)+ 1):
                skak = issue.issues(grade, difficulty)
                sk[str(i)] = skak['sk']
                ak[str(i)] = skak['ak']
            self.write(sk)
            t0 = timeit.default_timer()

        if (task == "request_result"):
            t0 = timeit.default_timer()
            # 计时结束
            # 批改答案
            error_amount = 0
            for i in range(1, int(number) + 1):
                student_ak=int(self.get_argument('i'))
                if student_ak!= ak[i]:
                    error_amount += 1
            accuracy = 1 - float(error_amount) / float(int(number))
            if accuracy >= 0.9:
                rate = 'A'
            elif accuracy >= 0.8:
                rate = 'B'
            elif accuracy >= 0.6:
                rate = 'C'
            else:
                rate = 'D'
            result={'error_amount': error_amount, 'accuracy': accuracy, 'rate': rate}
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
        pass


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
                    identification: str 表示用户ID
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
        self.write({"username": "熊猫王"})


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
        #con = pymysql.connect("127.0.0.1", "root", "lxt123", charset='utf8')

        #cur = con.cursor()
        ## 开始建库
        ## cur.execute("create database awesome character set utf8;")
        ## 使用库
        #cur.execute('use awesome;')
        ## 建表
        #cur.execute('''
        #     CREATE TABLE INFOM(id int unsigned primary key auto_increment not null,
        #     user_name CHAR(20) NOT NULL,passw CHAR(20))
        #    ''')
        #cur.close()
        #con.close()
    http_server = httpserver.HTTPServer(application)
    http_server.listen(8080)
    ioloop.IOLoop.current().start()
