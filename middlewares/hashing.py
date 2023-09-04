import bcrypt

# Function to hash a password
def hash_password(password, salt = None):    
    if salt is None:
        # Generate a salt
        salt = bcrypt.gensalt()
    
    # Hash the password using the salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    
    return hashed_password, salt

