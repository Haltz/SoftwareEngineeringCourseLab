import zhu
import pymysql

# 库名：test 表名：user

con = pymysql.connect("127.0.0.1", "root", "lxt123", charset='utf8')

cur = con.cursor()
# 开始建库

cur.execute("create database test character set utf8;")

# 使用库

cur.execute('use test;')
# 建表，若表存在先删除再建
cur.execute('''DROP TABLE IF EXISTS 'user' ''')

cur.execute('''

 CREATE TABLE 'user'(id int unsigned primary key auto_increment not null,

 user_name CHAR(20) NOT NULL,passw CHAR(20),emailm CHAR(20))

 ''')

cur.close()
con.close()

user_name1 = "cjm"
passw1 = "111111"
emailm1 = "222222"
user_name2 = "cjm"
passw2 = "111112"
emailm1 = "222222"

zhu.zhuce(user_name1, passw1, emailm1)

zhu.denglu(user_name2, passw2)
