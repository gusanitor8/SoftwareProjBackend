import bcrypt

# Function to hash a password
def hash_password(password, salt = None):    
    if salt is None:
        # Generate a salt
        salt = bcrypt.gensalt()
    else:
        salt = bytes.fromhex(salt)

    
    # Hash the password using the salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    salt_hex = salt.hex()
    hashed_pw_hex = hashed_password.hex()

    return hashed_pw_hex, salt_hex

