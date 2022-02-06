import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', password='jamesjh1984', database='james')

cursor = conn.cursor()

result = cursor.execute('SELECT * FROM website')

# data = cursor.fetchone()
# data = cursor.fetchmany(2)
data = cursor.fetchall()

print(data)

conn.close()