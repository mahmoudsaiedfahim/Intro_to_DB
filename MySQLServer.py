import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="mahmoud",
        password="Myfatma$123456",
        #database="sales",
        auth_plugin='mysql_native_password'  # Specify the authentication plugin
        #auth_plugin='caching_sha2_password'  # Specify the authentication plugin
        
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")
    mycursor.close()
    mydb.close()
except mysql.connector.Error as e:
    print(e)