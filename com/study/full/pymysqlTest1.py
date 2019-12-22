"""
https://mp.weixin.qq.com/s?__biz=MzU1NDk2MzQyNg==&mid=2247484186&idx=1&sn=cc72de1dc17f6f459eac310ef742c470&chksm=fbdadb97ccad5281764bec251e93645b0fd3451d4a54ebed53cbceab3bdf9ee9520f9c53d23f&scene=21#wechat_redirect

"""
import pymysql
import logging

# 打开数据库连接
conn = pymysql.connect(host="127.0.0.1",
                       port=3306,
                       user="root",
                       password="123456",
                       database="user",
                       charset="utf8")
print(conn)
print(type(conn))
# 获取连接下的游标
cursor_test = conn.cursor()
print(cursor_test)

# 使用 execute()  方法执行 SQL 查询，查询数据库版本
cursor_test.execute("SELECT VERSION()")

# 使用 fetchone() 方法返回一条数据.
data = cursor_test.fetchone()

print("Database version : %s " % data)

msg = "abc:%s" % 33
logging.info(msg)

# 关闭数据库连接
conn.close()
