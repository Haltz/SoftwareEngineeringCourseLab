# user_name:用户名 passw:密码
# 注册
import pymysql

def zhuce(user_name1, passw1): #返回0表示注册成功，1表示不成功
    db = pymysql.connect(host="localhost", user="root", password="123456", db="INFOM", port=3306, charset='utf8')
    # 使用cursor()方法获取操作游标
    cur = db.cursor()
    sql_insert = """insert into INFOM(id, user_name, passw,) values(0,user_name1,passw1,)"""
    try:
        cur.execute(sql_insert)
        # 提交
        db.commit()
    except Exception as e:
        # 错误回滚
        db.rollback()
        return 1
    finally:
        db.close()
    return 0
