import cx_Oracle

# cx_Oracle.init_oracle_client(lib_dir=r"D:\IT\Oracle\Oracle_Instant_Client\instantclient_19_14")

conn = cx_Oracle.connect('c##e519013/Day_202200412$@localhost:1521/orcl')

cursor = conn.cursor()

result = cursor.execute('SELECT * FROM website')

data = cursor.fetchone()
# data = cursor.fetchmany(2)
# data = cursor.fetchall()

print(data)

conn.close()