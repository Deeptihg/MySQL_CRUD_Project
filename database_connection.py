import mysql.connector
from mysql.connector import Error

try:
    # Establish the connection
    connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='res'
)


    # Check if the connection was successful
    if connection.is_connected():
        db_info = connection.get_server_info()
        print("Connected to MySQL Server version", db_info)
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print("You're connected to database:", record)

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    # Close the connection when done
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
