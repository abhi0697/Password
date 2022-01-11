from json import load
import os

with open(os.path.join(os.path.dirname(__file__), "password_schema.json"), 'r') as json_data:
                policy = load(json_data)
                spcl_char = policy['symbol']
                uppercaseletter = policy['uppercase']
                lowercaseletter = policy['lowercase']
                number = policy['numerical']
                symbols = policy['specialcharacters']
                pass_len = policy['minlength']
                all_article = policy['articles']

# Validating the generated password with the policy defined in the password_schema.json file
def validate(password):
    try:
        count=0
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










# def validate(password):
#     with open(os.path.join(os.path.dirname(__file__), "password_schema.json"), 'r') as json_data:
#             policy = load(json_data)
#             print(policy)
#             count=0
#             spcl_char = policy['symbol']
#             uppercaseletter = policy['uppercase']
#             lowercaseletter = policy['lowercase']
#             number = policy['numerical']
#             symbols = policy['specialcharacters']
#             pass_len = policy['minlength']
#             all_article = policy['articles']

#             if len(password) < pass_len:
#                 count=1
#                 return jsonify(
#                     {'message': 'Make Sure That Your Password Should at least Contain letters ' + str(pass_len)})

#             if number is True:
#                 if any(str.isdigit(password) for password in password) != number:
#                     count=1
#                     return jsonify({'message': 'Make Sure Your Password Should Contain One Number'})

#             if uppercaseletter is True:
#                 if any(password.isupper() for password in password) != uppercaseletter:
#                     count=1
#                     return jsonify({'message': 'Make Sure Your Password Should Contain One Uppercase Letter'})

#             if lowercaseletter is True:
#                 if any(password.islower() for password in password) != lowercaseletter:
#                     count=1
#                     return jsonify({'message': 'Make Sure Your Password Should Contain One Lowercase Letter'})

#             if spcl_char is True:
#                 if any(cha in symbols for cha in password) != True:
#                     count=1
#                     return jsonify({'message': 'Make Sure Your Password Should Contain One Special Characters'})

#             if any(cha not in all_article for cha in password):
#                 count=1
#                 return jsonify({'message': 'Make sure that you Have Entered The Allowed Characters'})

#             if count==1:
#                 print("password is invalid!!!")
#             if count==0:
#                 print("Password is valid!!!!")
# validate(password)