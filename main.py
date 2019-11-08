from tornado import web,ioloop,httpserver
import json, urllib3
import time,timeit
import os

state=0 #记录登录状态
now_user_name=''  #现在的用户名
grade =0 #现在的年级

# 定义视图处理函数
# 主页（选择哪种页面或者登录注册？）
class IndexHandler(web.RequestHandler):
    # 重写get处理方式
    def get(self,*args,**kwargs):
        # 想客户端发送一个数据
        self.render("index.html")

    def post(self,*args,**kwargs):
        name = self.get_argument('name')
        password = self.get_argument('password')
        # ret = "success"
        ret={"result":"success"}
        self.write(ret)

#做题页面（设置题目界面在哪？）
class QuestionanswerHandler(web.RequestHandler):
    def get(self,*args,**kwargs):
        self.render("questionanswer.html")
    #传用户选择的设置
    #生成题目并传到前端
    #开始计时
    t0 = timeit.default_timer()
    #开始计时

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
        self.render("person.html")

settings={
    'template_path':'templates','static_path':'static','static_url_prefix':'/static/', }
#设置路由
application = web.Application([
    (r'/index', IndexHandler),
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