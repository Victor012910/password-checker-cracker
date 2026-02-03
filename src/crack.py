# The goal of this file is to implement a dictionary attack against bcrypt hashes

# A dictionary attack is when a threat actor uses a dictionary or list of commonly used 
# words and phrases to gain unauthorized access to systems.


import bcrypt


def generate_hash(password: str) -> bytes:            
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)


def simulate_dictionary_attack(crack: bytes, dictionary: list[str]) -> str | None:
    for attempted_guess in dictionary:
        if bcrypt.checkpw(attempted_guess.encode(), crack):
            return attempted_guess
    return None 


 

mock_dictionary = ["qwerty", "password", "admin", "password123", "Ilovecats", "1223456", "abc123", "1234567890"]

hashed_password = input("Please enter your password. ")
user_input = generate_hash(hashed_password)

if hashed_password in mock_dictionary:
    print(f"WARNING! Your password is used frequently!: {hashed_password}, {user_input.decode()}")
else:
    print("Password is not found in commonly used list.")


# password1 = "qwerty"   
# hashed_password = generate_hash(password1)
# print(f"This is just for a test only: {hashed_password.decode()}")
# mock_dictionary = ["qwerty", "password", "admin", "password123", "Ilovecats", "1223456", "abc123", "1234567890"]


# found = simulate_dictionary_attack(hashed_password, mock_dictionary)

# if found:
#     print(f"Password found: {found}")
# else:
#     print("Password not found.")
    



