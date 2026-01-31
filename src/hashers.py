# The goal of this file is to implement the SHA-256 Password Hasher

import bcrypt 

# password = input("Create a pwd")
password = "nathan"

bytes = password.encode('utf-8')
salt = bcrypt.gensalt()
hash = bcrypt.hashpw(bytes, salt)


print(hash)