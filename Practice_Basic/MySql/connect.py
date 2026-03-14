import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="poshan_tracker"
)


# print(mydb)


mycursor = mydb.cursor()


# mycursor.execute("CREATE DATABASE mydatabase")


# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#   print(x)




try: 
    sql = "INSERT INTO pt_awc_users (name, mobile_number) VALUES (%s, %s)"
    val = ("John", "8410107875")
    mycursor.execute(sql, val)
    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
    
except Exception as e:
    print("Exception:", e)



# mycursor.execute("SELECT * FROM pt_awc_users LIMIT 5")
# mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)
