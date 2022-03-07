import psycopg2

conn = psycopg2.connect(host="localhost", port="5432", user="postgres", password="postgres", database="james")

cursor = conn.cursor()

cursor.execute('SELECT * FROM website')

for row in cursor:
    print(row)

cursor.close()
conn.close()