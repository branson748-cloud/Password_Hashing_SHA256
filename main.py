import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def check_password(stored_hash, user_password):
    return stored_hash == hash_password(user_password)

# Demo
password = input("Create password: ")
stored_hash = hash_password(password)

print("\nHashed Password:")
print(stored_hash)

login = input("\nEnter password to login: ")

valid_input = False

while not valid_input:
    if check_password(stored_hash, login):
        print("Access granted")
        valid_input = True
    else:
        print("\nWrong password, please try again")
        login = input("\nEnter password to login: ")