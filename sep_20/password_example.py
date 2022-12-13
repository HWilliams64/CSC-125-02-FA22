# Encoding
# Encryption = two way street => data => encrypted => data 
# Hashing = one way street => data => hashed 

import hashlib
my_password = "password123"
hashed_password = hashlib.sha256(my_password.encode("utf-8")).hexdigest()
print(hashed_password)

user_input = input("Please type your password: ")
hashed_user_input = hashlib.sha512(user_input.encode("utf-8")).hexdigest()
print(hashed_user_input)
print(f"Match: {hashed_password == hashed_user_input}")
