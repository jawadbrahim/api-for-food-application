import bcrypt

class HashingPassword:
    def hash_password(self, value):
        salt = bcrypt.gensalt()  # Generate a salt
        hashed = bcrypt.hashpw(value.encode('utf-8'), salt)  # Hash the password with the salt
        return hashed.decode('utf-8')  # Return the hashed password as a string

    def verify_password(self, provided_password, stored_password):
        # Check if the provided password matches the stored hashed password
        return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password.encode('utf-8'))
