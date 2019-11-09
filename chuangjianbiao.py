import pymysql
# 创建表
conn = pymysql.connect(host="localhost", user="root", password="123456", db="INFOM", port=3306, charset='utf8')
cur = conn.cursor()

cur.execute("""
create table if not EXISTS user
(
  CREATE TABLE INFOM(
    id int unsigned primary key auto_increment not null,
    user_name CHAR(20) NOT NULL,
    passw CHAR(20),
)
""")

cur.close()
conn.close()