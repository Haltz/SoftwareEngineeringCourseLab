from tornado import web,ioloop,httpserver
import json, urllib3
import time,timeit
import issue
import os

state=0 #记录登录状态
now_user_name=''  #现在的用户名
now_user_id=0

# 定义视图处理函数
# 主页（选择哪种页面或者登录注册？）
class IndexHandler(web.RequestHandler):
    # 重写get处理方式
    def get(self,*args,**kwargs):
        # 想客户端发送一个数据
        self.render("index.html")
    def post(self):
        exit=self.get_argument(exit)
        if exit==1:
            state=0
            now_user_name = ''

#登录和注册数据怎么区分？
class LoginHandler(web.RequestHandler):
    def get(self,*args,**kwargs):
        # 想客户端发送一个数据
        self.render("login.html",ret='ret')
    def post(self,*args,**kwargs):
        name = self.get_argument('name')
        password = self.get_argument('password')
        #调用数据库函数检查密码是否正确
        # ret = "success"
        ret={"result":"success"}
        self.write(ret)

#做题页面
class QuestionanswerHandler(web.RequestHandler):
    def get(self,*args,**kwargs):
        self.render("questionanswer.html",sk='sk')
    #传用户选择的设置
        chose=json.loads(self.request.body)
    #生成题目并传到前端
        sk={}
        ak={}
        for i in range(1,chose['number']+1):
            skak=issue.issues(chose['grade'],chose['mode'])
            sk[i]=skak['sk']
            ak[i]=skak['ak']
        self.write(sk)
    # 开始计时
        t0 = timeit.default_timer()
    #接受答案
        student_ak = json.loads(self.request.body)
    #计时结束
    #批改答案
        error_amount=0
        for i in range(1, chose['number'] + 1):
            if student_ak[i]!=ak[i]:
                error_amount+=1
        accuracy=1-float(error_amount)/float(chose['number'])
        if accuracy>=0.9:
            rate='A'
        elif accuracy>=0.8:
            rate='B'
        elif accuracy>=0.6:
            rate='C'
        else:
            rate='D'
    #返回结果
        return {'error_amount':error_amount,'accuracy':accuracy,'rate':rate}
    #数据记录到数据库中


#休闲页面
class RelaxHandler(web.RequestHandler):
    def get(self,*args,**kwargs):
        self.render("relax.html")

#复习页面（做题记录和错题列表）
class ReviewHandler(web.RequestHandler):
    def get(self,*args,**kwargs):
        self.render("review.html")

#个人主页   账户（ID，昵称，年级未显示？，做题记录）
class PersonHandler(web.RequestHandler):
    def get(self,*args,**kwargs):
        self.render("person.html",info='info')
        #从数据库获取当前用户信息
        #反馈给前端

settings={
    'template_path':'templates','static_path':'static','static_url_prefix':'/static/', }
#设置路由
application = web.Application([
    (r'/index', IndexHandler),
    (r'/login', LoginHandler),
    (r'/person', PersonHandler),
    (r'/questionanswer', QuestionanswerHandler),
    (r'/relax', RelaxHandler),
    (r'/review', ReviewHandler),
        ],**settings
    )


if __name__ == '__main__':
    http_server=httpserver.HTTPServer(application)
    http_server .listen(8080)
    ioloop.IOLoop.current().start()