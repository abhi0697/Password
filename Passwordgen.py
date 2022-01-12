import secrets
from validation import validate
from AES_encryption import aes_cbc_encrypt
from json import load
import os
import jwt
from flask import Flask, request


key=open('Secret_key.txt','r')
key=key.read().encode('utf8')
app = Flask(__name__)
app.config['SECRET_KEY']='Asecretkey1124'

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

# MySQL connection
from MySQL_connection import Mysql_connect
connection=Mysql_connect()

# Token authentication
# def token_auth():
#     token = None
#     if 'token' in request.headers:
#         token = request.headers['token']
#     if not token:
#         return False
#     try:
#         jwt.decode(token, app.config['SECRET_KEY'], algorithms="HS256")
#         return True
#     except Exception as e:
#         print(e)
#         return False


# Getting the input from the user for number of password as num_pass and length of password as pswl
num_pass=int(input("Please enter the number of passwords you want to generate!!"+"\n"))
pswl=int(input("Please enter the length of password you want to create: "+"\n"))

# Reading password_policy from Json file Password_schema.json
with open(os.path.join(os.path.dirname(__file__), "password_schema.json"), 'r') as json_data:
                policy = load(json_data)
                all_article = policy['articles']

# Insert passwords into database
def insert_data(enpass):
    try:
        val=enpass
        insert_data_query="Insert into PMS.users(password) values(%s);"
        cursor=connection.cursor()
        cursor.execute(insert_data_query,(val,))
        connection.commit()
        print("Data inserted successfully!!"+"\n")
    except Exception as e:
        print(e)

 
# Generating the number of random password with the specified length by the user
@app.route('/generate_passw', methods=['POST'])
def password():
    try:
        for _ in range(0,num_pass):
            password = ''
            for _ in range(0,pswl):
                password += secrets.choice(all_article)
# Validating the password by callinf the validate function from validation.py and if the validation passes
# then insert the password into database else not
            if validate(password)==0:
                insert_data(aes_cbc_encrypt(key,password))
                print("Great!! Your password fulfills the policy!!!"+"\n")
            else:
                print("Please generate the password again with all validations!!"+"\n")
            return password
    except Exception as e:
        print(e)
    
for i in range(num_pass):
    password()

# If user wants to read the stored password 
print("Do you want to see your stored password in an encrypted form??"+"\n")
read_pass=input("Please enter Yes, if you want to see the stored password!!"+"\n")
if read_pass=='Yes':
    from MySql_operations import read_data, delete_data
    read_data()
else:
    print("\n"+"Thank you for using our password management system!!"+"\n\n")
    exit()

# If user wants to delete a stored password
print("Do you want to delete your stored password??"+"\n")
delete_pass=input("Please enter Yes, if you want to delete the stored password!!"+"\n")
if delete_pass=='Yes':
    input_id=input("\n"+"Please enter the ID of the password you want to delete"+"\n")
    delete_data(input_id)
else:
    print("\n"+"Thank you for using our password management system!!"+"\n\n")
    exit()

#If the legitimate user is able to login then check for password validation after its generation.
if valid==True:
    def main():
        if __name__ == '__main__':
             app.run()
