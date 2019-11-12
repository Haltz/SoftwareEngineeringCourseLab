import zhu1
import pymysql
import db

# # 库名：info 表名：user
#
con = pymysql.connect("127.0.0.1", "root", "lxt123", charset='utf8')
#
cur = con.cursor()
# # 开始建库
#cur.execute("create database info character set utf8;")

# # 使用库
#
cur.execute('use info;')
# # 建表，若表存在先删除再建
# cur.execute('''DROP TABLE IF EXISTS 'user' ''')
#
#cur.execute('''

#   CREATE TABLE user(id int unsigned primary key auto_increment not null,
#   user_name CHAR(20) NOT NULL,test_id CHAR(20),test_limit_time CHAR(20),
#   test_difficulty CHAR(20),test_usetime CHAR(20),test_number CHAR(20),
#   test_wrong_number CHAR(20),test_accuracy CHAR(20),test_test_level CHAR(20))
   
#''')

cur.close()
con.close()

user_name1 = "zzzzx"
passw1 = "111111"
emailm1 = "222222"
user_name2 = "lxt"
passw2 = "111112"
test_id1 = "aaa"
test_limit_time1 = "aaa"
test_difficulty1 = "aaa"
test_usetime1 = "aaa"
test_number1 = "aaa"
test_wrong_number1 = "aaa"
test_accuracy1 = "aaa"
test_test_level1 = "aaa"

zhu1.insert_one(user_name1, test_id1, test_limit_time1, test_difficulty1, test_usetime1, test_number1,test_wrong_number1, test_accuracy1, test_test_level1)
# cur.execute("insert into user(user_name,passw,emailm) values(user_name1,passw1,emailm1)")
zhu1.present_all(user_name1)
