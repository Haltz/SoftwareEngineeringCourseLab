#user_name:用户名 passw:密码
#登陆
import pymysql

def denglu(user_name1, passw1): #返回0表示登陆成功，1表示不成功
#打开数据库连接
    db= pymysql.connect(host="localhost",user="root",password="123456",db="INFOM",port=3307,charset='utf8')
# 使用cursor()方法获取操作游标
    cur = db.cursor()
# 编写sql 查询语句  INFOM 对应我的表名
    sql = "select * from INFOM where user_name = 'user_name'" #查询用户名是否存在
    try:
        cur.execute(sql)  # 执行sql语句
        results = cur.fetchall()  # 获取查询的所有记录
        for row in results:
            id = row[0]
            user_name_ = row[1]
            passw_ = row[2]
        if passw1 == passw_:
            return 0
        else:
            return 1
    except Exception as e:
        raise e
    finally:
        db.close()  # 关闭连接
