import mysql.connector
import pymysql
import work01

Code_List = work01.get_activation_code(work01.CODE_LENGTH, work01.CODE_NUM)

my_db = pymysql.connect(
    host='rm-wz9d4iopy2m6549id8o.mysql.rds.aliyuncs.com',
    port=3306,
    user='qimu_0527',
    passwd='qimu_0527',
    db='exercise0002'
)

my_cursor = my_db.cursor()
my_cursor.execute('DROP TABLE IF EXISTS Ning_activation_code')

SQL_CreatTable = '''CREATE TABLE Ning_activation_code(NUM INT NOT NULL, 
                        Code CHAR(30), 
                        Used BOOLEAN)'''
my_cursor.execute(SQL_CreatTable)

for i in range(len(Code_List)):
    SQL_INSERT = '''INSERT INTO Ning_activation_code (NUM, Code, Used) VALUES (%s , '%s', 0)''' % (str(i+1),Code_List[i])

    my_cursor.execute(SQL_INSERT)

my_db.commit()
my_db.close()
