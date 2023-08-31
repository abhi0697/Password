# Password
Password management system

Step 1: Install MySQL and create a user with username: singh, and password: 7602
Step 2: Create the database and table using the commands in file named: MySQL DBtable.txt
Step 3: Install and import all the desired libraries like, flask, decouple, json, jwt etc. 
Step 4: trace to the desired folder and run the command: "flask run"
	The python flask app will automatically connect to MySQL database.

Using the localhost we can work with API and call them to see their desired outputs.

The APIs and their outputs are discussed thoroughly in the report of project.

For example: 
running 127.0.0.1/ in the browser will show a message welcoming the user to PMS.
"127.0.0.1/get_userid" will the user IDs stored in the database.
"127.0.0.1/delete_passw/<user_id>" could be used to delete the userID and corresponding password.
"127.0.0.1/generate_passw/<int:num_pass>/<int:pswl>" could be used to generate a desired number of password with their desired length. 

