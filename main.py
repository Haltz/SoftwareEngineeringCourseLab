from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop
import json, urllib3


# 定义视图处理函数

class IndexHandler(RequestHandler):
    # 重写get处理方式
    def get(self):
        # 想客户端发送一个数据
        self.render("index.html")
    
    def post(self):
        print(self.get_argument("name",""))
        print(self.get_argument("password",""))
        # ret = "success"
        ret={"result":"success"}
        self.write(ret)
        


# 程序入口
if __name__ == '__main__':
    app = Application([
        # 定义路由访问
        (r'/index', IndexHandler),
    ])
    # 监听端口
    app.listen(8000)
    # 启用tornado内置的服务器轮询监听
    IOLoop.current().start()