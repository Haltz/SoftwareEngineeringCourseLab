import db1

def insert_one(user_name1, test_id1, test_limit_time1, test_difficulty1,
               test_usetime1, test_number1, test_wrong_number1, test_accuracy1, test_test_level1):
    # 输入某个用户名某次的错误信息
    insert_sql = """ insert into user(user_name, test_id, test_limit_time,test_difficulty,test_usetime,test_number, test_wrong_number,test_accuracy, test_test_level) values("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s") """ % (
    user_name1, test_id1, test_limit_time1, test_difficulty1, test_usetime1, test_number1, test_wrong_number1,test_accuracy1, test_test_level1)
    # insert_sql = """ insert into user(user_name,test_id, test_limit_time, test_difficulty,test_usetime, test_number, test_wrong_number, test_accuracy, test_test_level) values("%s", "%s", "%s","%s","%s","%s","%s","%s","%s") """ % (user_name1,test_id1,test_limit_time1, test_difficulty1,test_usetime1, test_number1, test_wrong_number1,test_accuracy1, test_test_level1)
    print(insert_sql)
    db1.insert_or_update_data(insert_sql)
    print("插入错误记录成功")  # 可换成返回参数
    return


def present_all(user_name1):
    # 查讯某个用户所有错误信息
    query_sql = "select * from user where user_name = '%s'" % (user_name1)
    print(query_sql)
    get_result = db1.query_data(query_sql)
    # 返回一个列表，列表中元素是字典，如{id:XX,user_name:XX,}
    print(get_result)
    if len(get_result):  # 列表不为空
        return get_result
    else:
        print("不存在该用户")
        return 0
