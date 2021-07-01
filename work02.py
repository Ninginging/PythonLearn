import mysql.connector
#import work01

mydb = mysql.connector.connect(
    host='db4free.net',  # 数据库主机地址
    port=3306,
    user='wangfei',      # 数据库用户名
    passwd='12345678',   # 数据库密码
    db='wangfei_db'
)


mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")
mydb.commit()
table=mycursor.fetchall()

for x in mycursor:
    print(x)
