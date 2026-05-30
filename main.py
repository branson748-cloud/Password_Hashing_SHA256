import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def check_password(stored_hash, user_password):
    return stored_hash == hash_password(user_password)

# Create password
password = input("Create password: ")
stored_hash = hash_password(password)

print("\nHashed Password:")
print(stored_hash)

# Login
attempts = 3

while attempts > 0:
    login = input("\nEnter password: ")

    if check_password(stored_hash, login):
        print("Access granted")
        break

    attempts -= 1

    if attempts > 0:
        print(f"Incorrect password, {attempts} {'attempt' if attempts == 1 else 'attempts'} left")
    else:
        print("Access denied")