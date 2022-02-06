import psycopg2

conn = psycopg2.connect(host="localhost", port="5432", user="postgres", password="postgres", database="james")

cursor = conn.cursor()

result = cursor.execute('SELECT * FROM website')

# data = cursor.fetchone()
# data = cursor.fetchmany(2)
data = cursor.fetchall()

print(data)

conn.close()