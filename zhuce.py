# user_name:用户名 passw:密码
# 注册
import pymysql

def zhuce(user_name1, passw1,email1):
    #返回0表示注册成功，非0表示不成功

    db = pymysql.connect(host="127.0.0.1", user="root", password="lxt123", db="awesome", port=3306, charset='utf8')
    # 使用cursor()方法获取操作游标

    cur = db.cursor()
    cur.execute('use awesome;')
    sql_insert = """insert into INFOM2(user_name, passw,email) values(user_name1,passw1,email1)"""
    try:
        cur.execute(sql_insert)
        # 提交

        db.commit()
    except Exception as e:
        # 错误回滚

        db.rollback()
    finally:
        cur.close()
        db.close()
    return 0


