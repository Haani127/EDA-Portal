import pymysql

conn = pymysql.connect("localhost","rootuser","rootuser","rootuser")
cursor = conn.cursor()

order_id = input()

query = "SELECT * FROM Orders WHERE order_id = %s"
cursor.execute(query,(order_id,))

record = cursor.fetchall()

print("Order Details:")

for i in record:
    print(i)

cursor.close()
conn.close()
