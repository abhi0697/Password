from MySQL_connection import Mysql_connect
connection=Mysql_connect()

# Function to read the encryoted from database
def read_data():
    try:
        show_passw="Select * from users;"
        cursor=connection.cursor()
        cursor.execute(show_passw)
        records = cursor.fetchall()
        print("Total number of rows in table: ", cursor.rowcount)
        print("\nPrinting each row"+"\n")
        for row in records:
            print("Username= ", row[0], )
            print("Password = ", row[1])
            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬"+"\n")
    except Exception as e:
        print(e)

# Function to delete the encrypted password using the UserID
def delete_data(del_id):
    try:
        val=del_id
        delete_passw="Delete from users where userid=%s;"
        cursor=connection.cursor()
        cursor.execute(delete_passw,(val,))
        connection.commit()
        print("The password of UserID "+val+" has been deleted!!!"+"\n\n")
    except Exception as e:
        print(e)