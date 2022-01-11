import unittest
from Passwordgen import insert_data, password
from validation import validate
from DES_encryption import des_cbc_encrypt
from MySql_operations import read_data, delete_data
from check_pwned import pwnedpassword

class PMSTesting(unittest.TestCase):
    
    def setUp(self):
        self.passw='ASdfghgf12!@asd'
        self.passfalse='a1s2a'
        self.encr=b'\x90\x91U\xff\x88\xa2\xaa\xb1\x18\xb5?tA\xa5\xee\x02\xb9\x7f\xc3\x97\xfew%#'
        self.pwned='b7c54'
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
        self.assertTrue(des_cbc_encrypt,self.passw)

# This testing checks the pwnedpassword() function in passwordgen is checking the password is compromised or not!!
    def test_pwnedpass(self):
        self.assertTrue(pwnedpassword,self.encr)

# This testing checks the insert_data() function in passwordgen is saving encrypted password in Database or not!!
    def test_insert_data(self):
        self.assertTrue(insert_data,self.encr)

# This testing checks the read_data() function in passwordgen is fetching passwords from Database or not!!     
    def test_read_data(self):
        self.assertTrue(read_data)

# This testing checks the delete_data() function in passwordgen is deleting password with respect to a UserID or not!!   
    def test_delete_data(self):
        self.assertTrue(delete_data,self.delete)

# This teardown function will help the test code to be clean and flexible after all test cases are executed.
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
