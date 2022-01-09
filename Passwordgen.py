import random
import mysql.connector
from mysql.connector import Error
import bcrypt
import requests
from json import load
import os
from flask import Flask


app = Flask(__name__)
api_url = "https://api.pwnedpasswords.com/range/"

#user login to create password
print("Please login here to create a password!!!"+"\n")

#lguser will accept the username of legitimate user
#lgpass will accept the password of legitimate user
lguser=input("Enter your username! "+"\n")
lgpass=input("Enter your password! "+"\n")
valid=False
if lguser=='admin' and lgpass=='admin':
    print("login Successfull!!"+"\n")
    print("☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺"+"\n")
    valid=True
else:
    print("Invalid Credentials!!"+"\n")
    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    exit()

Db_pass=input("Please enter the MySQL Server password to connect to the database."+"\n")

# MySQL connection
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='PMS',
                                         user='singh',
                                         password=Db_pass)
    
    if connection.is_connected():
        db_Info = connection.get_server_info()
    print("Connected to MySQL Server version ", db_Info)
    cursor = connection.cursor()
    cursor.execute("select database();")
    record = cursor.fetchone()
    print("You're connected to database: ", record)
except Error as e:
    print("Error while connecting to MySQL", e)
    exit()

# list of all the characters that could be used in generating a password
articles = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()}{[]<>,/\.')

# Getting the input from the user for number of password as num_pass and length of password as pswl
num_pass=int(input("Please enter the number of passwords you want to generate!!"+"\n"))
pswl=int(input("Please enter the length of password you want to create: "+"\n"))


# check validation of the password
def validate(password):
    try:
        with open(os.path.join(os.path.dirname(__file__), "password_schema.json"), 'r') as json_data:
                policy = load(json_data)
                policy_backup=policy
                # print(policy)
                count=0
                spcl_char = policy['symbol']
                uppercaseletter = policy['uppercase']
                lowercaseletter = policy['lowercase']
                number = policy['numerical']
                symbols = policy['specialcharacters']
                pass_len = policy['minlength']
                all_article = policy['articles']
                if len(password) < pass_len:
                    count=1
                    print("Please enter at least password of 8 characters!!"+"\n")

                if number is True & any(str.isdigit(password) for password in password) != number:
                    count=1
                    print("Please enter at least one numerical in your password!!"+"\n")

                if uppercaseletter is True & any(password.isupper() for password in password) != uppercaseletter:
                    count=1
                    print("Please enter at least one uppercase letter in your password!!"+"\n")

                if lowercaseletter is True & any(password.islower() for password in password) != lowercaseletter:
                    count=1
                    print("Please enter at least one lowercase letter in your password!!"+"\n")

                if spcl_char is True & any(char in symbols for char in password) != True:
                    count=1
                    print("Please enter at least one special character in your password!!"+"\n")
                        
                if not any(char in all_article for char in password):
                    count=1
                    print("Please check if your password does not sastisfy password policy and generate again !!"+"\n")
                return count
    except Exception as e:
        print(e)

# Insert passwords into database
def insert_data(enpass):
    try:
        val=enpass
        insert_data_query="Insert into PMS.users(password) values(%s);"
        cursor=connection.cursor()
        cursor.execute(insert_data_query,(val,))
        connection.commit()
        print("Data inserted successfully!!")
    except Exception as e:
        print(e)

# Check pawned password!!
def pwnedpassword(hash_pass):
    try:
        # print(hashed_password)
        pwned_check=(hash_pass[9:14]).upper()
        # print(pwned_check)
        hex_convert=pwned_check.hex()[:5]
        # print(hex_convert)
        new_url=api_url+hex_convert
        print("New URL:"+new_url)
        response=requests.get(new_url)
        print(response.status_code)
        res_five=response.text[5:]
        if hex_convert==res_five:
            print("You have been pawned!!"+"\n")
        else:
            print("Your password is safe and ready to be saved in the database!!!!"+"\n")
        print("Your password is safe!!")
    except Exception as e:
        print(e)
    
#Hashing password 
def hashing(plaintext):
    try:
        plainbytes= bytes(plaintext, 'utf8')
        salt = bcrypt.gensalt(12)
        hashed_password = bcrypt.hashpw(plainbytes, salt)
        pwnedpassword(hashed_password)
        return hashed_password
    except Exception as e:
        print(e)

# Generating the number of random password with the specified length by the user
@app.route('/generate_passw', methods=['POST'])
def password():
    try:
        for _ in range(0,num_pass):
            password = ''
            for _ in range(0,pswl):
                password += random.choice(articles)
            # print(password)
            if validate(password)==0:
                insert_data(hashing(password))
                print("Great!! Your password fulfills the policy!!!"+"\n")
            else:
                print("Please generate the password again with all validations!!"+"\n")
            return password
    except Exception as e:
        print(e)
    
for i in range(num_pass):
    password()

# Fetch all values from sql table
@app.route('/get_password', methods=['GET'])
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
    except Exception as e:
        print(e)
        
@app.route('/delete_password', methods=['DELETE'])
def delete_data(del_id):
    try:
        val=del_id
        delete_passw="Delete from users where userid=%s;"
        cursor=connection.cursor()
        cursor.execute(delete_passw,(val,))
        connection.commit()
        print("The password of UserID "+val+" has been deleted!!!")
    except Exception as e:
        print(e)

# If user wants to read the stored password 
print("Do you want to see your stored password in an encrypted form??"+"\n")
read_pass=input("Please enter Yes, if you want to see the stored password!!"+"\n")
if read_pass=='Yes':
    read_data()
else:
    print("\n"+"Thank you for using our password management system!!")

# If user wants to delete a stored password
print("Do you want to delete your stored password??"+"\n")
delete_pass=input("Please enter Yes, if you want to delete the stored password!!"+"\n")
if delete_pass=='Yes':
    input_id=input("\n"+"Please enter the ID of the password you want to delete"+"\n")
    delete_data(input_id)
else:
    print("\n"+"Thank you for using our password management system!!")

#If the legitimate user is able to login then check for password validation after its generation.
if valid==True:
    def main():
        if __name__ == '__main__':
             app.run()
