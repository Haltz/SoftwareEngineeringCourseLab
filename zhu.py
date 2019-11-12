import db

def zhuce(user_name1, passw1, emailm1):
    # 给一个例子，可修改
    query_sql = "select * from user where user_name = '%s'" % (user_name1)
    get_result = db.query_data(query_sql)
    # 返回一个列表，列表中元素是字典，如{id:XX,user_name:XX,}
    if len(get_result):  # 列表不为空
        print("用户名已存在，请重新注册")
        return
    else:
        insert_sql = """ insert into user(user_name, passw, emailm) values("%s", "%s", "%s") """ % (
        user_name1, passw1, emailm1)
        # insert_sql = ' insert into user(user_name, passw, emailm) values(\" ' + user_name1 + '\",\"' + passw1 + '\",\"' + emailm1 + "\") "
        # print(insert_sql)
        db.insert_or_update_data(insert_sql)
        print("注册成功")  # 可换成返回参数
        return


def denglu(user_name1, passw1):
    # 登陆 需加传入参数user_name1、passw1字符串，即用户登陆输入
    # 给一个例子，可修改
    query_sql = "select * from user where user_name = '%s'" % (user_name1)
    get_result = db.query_data(query_sql)
    # 返回一个列表，列表中元素是字典，如{id:XX,user_name:XX,}
    if len(get_result):  # 列表不为空
        # print(get_result)
        if get_result[0]["passw"] == passw1:
            print("登陆成功")
            return 0
        else:
            print("登陆错误")
            return 1
    else:
        print("用户名输入错误")
        return 2


