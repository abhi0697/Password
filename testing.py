import unittest
from Passwordgen import delete_data, hashing, insert_data, read_data, validate, password, pwnedpassword

class PMSTesting(unittest.TestCase):
    
    def setUp(self):
        self.passw='ASdfghgf12!@asd'
        self.passfalse='a1s2a'
        self.hashed='$2b$12$6YalzUirJvpJCGKoDWTHk.uldaUZIozXiiLaG0Qtk36.MDdyx3pcq'
        self.pwned='56524'
        self.delete='124'

# This testing check the complexity of the password if it is NOT following the policy, if it does not follows then it will pass else fail!!
    def test_check_complexity_notpolicy(self):
        self.assertTrue(validate,self.passfalse)

# This testing check the complexity of the password if it follow the policy or not, if it follows then it will pass else fail!!
    def test_check_complexity_pass(self):
        self.assertTrue(validate,self.passw) 
        
# This testing checks the password() function in passwordgen is generating password or not!!
    def test_pass_generation(self):
        self.assertTrue(password)

# This testing checks the hashing() function in passwordgen is hashing the password or not!!
    def test_hashing(self):
        self.assertTrue(hashing,self.passw)

# This testing checks the pwnedpassword() function in passwordgen is checking the password is compromised or not!!
    def test_pwnedpass(self):
        self.assertTrue(pwnedpassword,self.hashed)

# This testing checks the insert_data() function in passwordgen is saving encrypted password in Database or not!!
    def test_insert_data(self):
        self.assertTrue(insert_data,self.hashed)

# This testing checks the read_data() function in passwordgen is fetching passwords from Database or not!!     
    def test_read_data(self):
        self.assertTrue(read_data)

# This testing checks the delete_data() function in passwordgen is deleting password with respect to a UserID or not!!   
    def test_delete_data(self):
        self.assertTrue(delete_data,self.delete)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
