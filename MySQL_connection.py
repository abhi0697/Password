import mysql.connector
from mysql.connector import Error

# Db_pass=input("Please enter the MySQL Server password to connect to the database."+"\n")
# Function for connection to MySQL server
def Mysql_connect():
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='PMS',
                                            user='singh',
                                            password='7602')
        
        if connection.is_connected():
            db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        return connection
    except Error as e:
        print("Error while connecting to MySQL", e)
        exit()