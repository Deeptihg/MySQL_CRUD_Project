import mysql.connector
from mysql.connector import Error

# Database connection details
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = ''
DB_NAME = 'res'

# Function to create a new record
def create_record(name, email, dob, phone, address):
    try:
        connection = mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
        cursor = connection.cursor()
        sql = "INSERT INTO Registration (Name, Email, DateOfBirth, PhoneNumber, Address) VALUES (%s, %s, %s, %s, %s)"
        values = (name, email, dob, phone, address)
        cursor.execute(sql, values)
        connection.commit()
        print("Record inserted successfully.")
    except Error as e:
        print("Error inserting data:", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Function to read records
def read_records():
    try:
        connection = mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Registration")
        results = cursor.fetchall()
        for row in results:
            print(row)
    except Error as e:
        print("Error reading data:", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Function to update a record
def update_record(name, new_phone):
    try:
        connection = mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
        cursor = connection.cursor()
        sql = "UPDATE Registration SET PhoneNumber = %s WHERE Name = %s"
        values = (new_phone, name)
        cursor.execute(sql, values)
        connection.commit()
        print("Record updated successfully.")
    except Error as e:
        print("Error updating data:", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Function to delete a record
def delete_record(name):
    try:
        connection = mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
        cursor = connection.cursor()
        sql = "DELETE FROM Registration WHERE Name = %s"
        values = (name,)
        cursor.execute(sql, values)
        connection.commit()
        print("Record deleted successfully.")
    except Error as e:
        print("Error deleting data:", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Example usage
if __name__ == "__main__":
    create_record('John Doe', 'john.doe@example.com', '1995-06-15', '1234567890', '123 Elm St')
    read_records()
    update_record('John Doe', '0987654321')
    delete_record('John Doe')
