import pymysql
# 创建表
con = pymysql.connect("127.0.0.1","root", "lxt123", charset='utf8')

cur = con.cursor()
# 开始建库
#cur.execute("create database awesome character set utf8;")
# 使用库
cur.execute('use awesome;')
# 建表
cur.execute('''
 CREATE TABLE INFOM2(id int unsigned primary key auto_increment not null,
 user_name CHAR(20) NOT NULL,passw CHAR(20),
 email CHAR(40))
 ''')


#create table if not EXISTS user
#(
#  CREATE TABLE INFOM(
#    id int unsigned primary key auto_increment not null,
#    user_name CHAR(20) NOT NULL,
#    passw CHAR(20),
#)
cur.close()
con.close()