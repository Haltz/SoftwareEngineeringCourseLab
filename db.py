import pymysql
#库名：test 表名：user
def get_conn(): #获取连接,return: mysql connection
    return pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="lxt123",
        database="test", #库名
        charset="utf8"
    )

def query_data(sql):
# 根据sql查询数据并返回
# return：list[dict]
    conn = get_conn()
    try:
        cursor = conn.curcsor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        return cursor.fetchall()
    finally:
        conn.close()

def insert_or_update_data(sql):
    #新增数据
    #return:不返回内容
    conn = get_conn()
    try:
        cursor = conn.curcsor()
        cursor.execute(sql)
        conn.commit()
    finally:
        conn.close()