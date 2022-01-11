import requests
api_url = "https://api.pwnedpasswords.com/range/"

# check for pwned passwords
def pwnedpassword(encr_pass):
    try:
        pwned_check=(encr_pass[9:14]).upper()
        hex_convert=pwned_check.hex()[:5]
        new_url=api_url+hex_convert
        print("New URL:"+new_url)
        response=requests.get(new_url)
        print(response.status_code)
        res_five=response.text[5:]
        if hex_convert==res_five:
            print("You have been pawned!!"+"\n")
        else:
            print("Your password is safe and ready to be saved in the database!!!!"+"\n")
        print("Your password is safe!!"+"\n")
    except Exception as e:
        print(e)
    