from validation import validate
from json import load
from decouple import config
import os
import jwt
import secrets
from flask import Flask, request, jsonify

key=open('Secret_key.txt','r')
key=key.read().encode('utf8')
app = Flask(__name__)
SECRET_KEY=config('Key')

#user login to create password 
@app.route('/login', methods=['POST'])
def login():
    username=request.get_json()['username']
    password=request.get_json()['password']
    user1=config('env_username')
    passw1=config('env_password')
    if username == user1 and password == passw1:
        return token(username)
    return "Invalid Credentials"

# MySQL connection
from MySQL_connection import Mysql_connect
connection=Mysql_connect()

# Token authentication
def token_auth(request):
    token = None
    if 'token' in request.headers:
        token = request.headers['token']
    if not token:
        return False
    try:
        jwt.decode(token, app.config['SECRET_KEY'], algorithms="HS256")
        return True
    except Exception as e:
        print(e)
        return False
    
def token(username):
    token = jwt.encode(
        {'public_id': username},
        SECRET_KEY, algorithm="HS256")
    return jsonify({'token': token})


# Reading password_policy from Json file Password_schema.json
with open(os.path.join(os.path.dirname(__file__), "password_schema.json"), 'r') as json_data:
                policy = load(json_data)
                all_article = policy['articles']

# Insert passwords into database
def insert_data(enpass):
    try:
        val=(enpass, key)
        insert_data_query="Insert into PMS.users(password) values(AES_ENCRYPT(%s, %s));"
        cursor=connection.cursor()
        cursor.execute(insert_data_query,val)
        connection.commit()
        print("Data inserted successfully!!"+"\n")
    except Exception as e:
        print(e)

# Generating the number of random password with the specified length by the user
@app.route('/generate_passw/<int:num_pass>/<int:pswl>', methods=['POST'])
def password(num_pass,pswl):
    try:
        for _ in range(0,num_pass):
            password = ''
            for _ in range(0,pswl):
                password += secrets.choice(all_article)
# Validating the password by callinf the validate function from validation.py and if the validation passes
# then insert the password into database else not
            if validate(password)==0:
                insert_data(password)
                return("Great!! Your password fulfills the policy!!!"+"\n")
            else:
                return("Please generate the password again with all validations!!"+"\n")
    except Exception as e:
        print(e)
    
# To read the userID of the saved passwords
@app.route('/get_userid', methods=['GET'])
def read_data():
    try:
        show_passw="Select userid from users;"
        cursor=connection.cursor()
        cursor.execute(show_passw)
        records = cursor.fetchall()
        fetched_data=[]
        print("Total number of rows in table: ", cursor.rowcount)
        for row in records:
            fetched_data.append(row)
        return jsonify({'UserID': fetched_data})
    except Exception as e:
        print(e)


# Function to delete the encrypted password using the UserID
@app.route('/delete_passw/<user_id>', methods=["DELETE"])
def delete_data(user_id):
    try:
        # val = request.get_json()
        val=user_id
        delete_passw="Delete from users where userid=%s;"
        cursor=connection.cursor()
        cursor.execute(delete_passw,(val,))
        connection.commit()
        return ("The password of UserID "+val+" has been deleted!!!"+"\n\n")
    except Exception as e:
        print(e)

#If the legitimate user is able to login then check for password validation after its generation.
if __name__ == '__main__':
    app.run(debug=True)