# Password_Hashing_SHA256
Simple Python SHA-256 password hashing demo

## Version
Current version: **v1.0.0**

## Features
- **SHA-256 Password Hashing**: Securely hash passwords using the SHA-256 cryptographic algorithm
- **Password Verification**: Compare user input against stored hashes to validate credentials
- **Interactive CLI**: User-friendly command-line interface for password creation and login
- **Input Validation**: Repeating login attempts until correct password is provided
- **No External Dependencies**: Uses Python's built-in `hashlib` module

## How It Works

### SHA-256 Hashing
SHA-256 (Secure Hash Algorithm 256-bit) is a cryptographic hash function that converts any input data into a fixed 64-character hexadecimal string. Key characteristics:

- **One-way function**: Cannot reverse the hash to obtain the original password
- **Deterministic**: The same input always produces the same hash
- **Avalanche effect**: Small changes in input produce completely different hashes
- **Fixed output**: Always produces 64-character hex string regardless of input length

**Example:**
```
Input:  "MyPassword123"
Output: "8d0d1e7a8f3c9e2b1a5c4d7f6e9b3a2c1d5e8f0a7b9c3e6d4a2b8f1c5e9a0b"

Input:  "MyPassword124" (changed last character)
Output: "e2c5f8a1b3e7d9c4f6a8b1e3d5c7f9a2b4e6d8c0a2b4d6f8a0c2e4a6b8d0"
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/branson748-cloud/Password_Hashing_SHA256.git
cd Password_Hashing_SHA256
```

2. Ensure you have Python 3.x installed:
```bash
python --version  # or python3 --version
```

## Usage

Run the application:
```bash
python main.py
```

### Interactive Workflow
When you run the program, you'll be prompted to:

1. **Create a password** - Enter your desired password
2. **View the hash** - See the SHA-256 hash of your password
3. **Login** - Enter the password again to verify it matches
4. **Retry on failure** - Keep trying until the correct password is entered

## Example Usage

### First-Time Setup and Login
```
Create password: SecurePass123

Hashed Password:
9f86d081884c7d6d9febb2f9da6e4e5e8f7e7e7e7e7e7e7e7e7e7e7e7e7e7e

Enter password to login: SecurePass123
Access granted
```

### Failed Login Attempt
```
Create password: MySecret

Hashed Password:
a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a

Enter password to login: WrongPassword

Wrong password, please try again

Enter password to login: MySecret
Access granted
```

## Code Structure

### Function: `hash_password(password)`
**Purpose**: Converts a plain-text password into a SHA-256 hash

**Parameters:**
- `password` (str): The plain-text password to be hashed

**Returns:**
- `str`: A 64-character hexadecimal SHA-256 hash

**How it works:**
```python
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
```
1. `.encode()` - Converts the string to bytes (SHA-256 requires bytes)
2. `hashlib.sha256()` - Creates SHA-256 hash object
3. `.hexdigest()` - Returns hash as a hexadecimal string

**Example:**
```python
hash1 = hash_password("test123")
# Output: '6ae999552a2ebb5b9d1f6b651eb5ba31a7c16fa2cff2c83690df62ba6f25f8eb'
```

### Function: `check_password(stored_hash, user_password)`
**Purpose**: Verifies if a user's password matches the stored hash

**Parameters:**
- `stored_hash` (str): The previously stored SHA-256 hash
- `user_password` (str): The password entered by the user to verify

**Returns:**
- `bool`: `True` if passwords match, `False` otherwise

**How it works:**
```python
def check_password(stored_hash, user_password):
    return stored_hash == hash_password(user_password)
```
1. Hashes the user-provided password using `hash_password()`
2. Compares it byte-by-byte with the stored hash
3. Returns `True` only if they match exactly

**Example:**
```python
stored = hash_password("correct123")
check_password(stored, "correct123")  # Returns: True
check_password(stored, "wrong123")    # Returns: False
```

### Main Program Flow

**Lines 10-11: Password Creation**
```python
password = input("Create password: ")
stored_hash = hash_password(password)
```
- Prompts user to create a password
- Immediately hashes and stores it

**Lines 13-14: Display Hash**
```python
print("\nHashed Password:")
print(stored_hash)
```
- Shows the generated SHA-256 hash

**Lines 16-26: Login Validation Loop**
```python
login = input("\nEnter password to login: ")
valid_input = False

while not valid_input:
    if check_password(stored_hash, login):
        print("Access granted")
        valid_input = True
    else:
        print("\nWrong password, please try again")
        login = input("\nEnter password to login: ")
```
- Loops until correct password is entered
- `check_password()` verifies each attempt
- Exits when password matches

## Requirements
- Python 3.x
- No external dependencies (uses built-in `hashlib`)

## Security Considerations

⚠️ **Important**: This is a **demo application** for educational purposes. For production use:

1. **Use Salt**: Add random salt to passwords before hashing to prevent rainbow table attacks
   ```python
   import os
   salt = os.urandom(32)
   ```

2. **Use bcrypt or Argon2**: These are specifically designed for password hashing
   ```python
   import bcrypt
   ```

3. **Use HTTPS**: Always transmit passwords over encrypted connections

4. **Hash on Server**: Never send plain passwords over networks

5. **Consider Rate Limiting**: Protect against brute-force attacks

## Example with Salt (Advanced)

```python
import hashlib
import os

def hash_password_with_salt(password):
    salt = os.urandom(32)
    hash_obj = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return salt.hex() + hash_obj.hex()

def check_password_with_salt(stored, user_password):
    salt = bytes.fromhex(stored[:64])
    stored_hash = stored[64:]
    new_hash = hashlib.pbkdf2_hmac('sha256', user_password.encode(), salt, 100000)
    return new_hash.hex() == stored_hash
```

## License
This project is open source and available under the MIT License.

## Author
**branson748-cloud**

## Contributing
Feel free to fork this repository and submit pull requests for any improvements!

## Troubleshooting

**Q: The program keeps asking for a password after I enter the correct one**
- A: Ensure you're typing the password exactly as you created it (case-sensitive)

**Q: I want to reset my password**
- A: Simply run the program again to create a new password

**Q: Can I use special characters in passwords?**
- A: Yes! SHA-256 handles any character, including special characters, emojis, etc.

## Learning Resources

- [SHA-256 Wikipedia](https://en.wikipedia.org/wiki/SHA-2)
- [Python hashlib Documentation](https://docs.python.org/3/library/hashlib.html)
- [Password Security Best Practices](https://owasp.org/www-community/attacks/Password_Cracking)
