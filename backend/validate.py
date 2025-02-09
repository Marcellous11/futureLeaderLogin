import bcrypt

class Auth:
    def __init__(self):
        pass

    
    @staticmethod
    def hash_password(password):
        salt = bcrypt.gensalt()  # Generate a new salt
        hashed = bcrypt.hashpw(password.encode(), salt)
        return hashed
    
    @staticmethod
    def verify_password(user,password):
        if user:  # Ensure the user exists
            stored_hashed_password = user[1]  # Extract the hashed password as a string
            if bcrypt.checkpw(password.encode(), stored_hashed_password):
                print("Password is correct!")
                return True
            else:
                print("Incorrect password.")
                return False
        else:
            print("User not found.")
            return False


    @staticmethod
    def email_already_exist():
        return 