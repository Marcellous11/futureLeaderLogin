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
    def verify_password(user,password)->bool:
        try:
            if user:  # Ensure the user exists

                stored_hashed_password = user["password"]
                print("Password ---->",user["password"])
                if bcrypt.checkpw(password.encode(), stored_hashed_password):
                    print("Auth: Password is correct!")
                    return True
                else:
                    print("Auth: Incorrect password.")
                    return False
            else:
                print("User not found.")
                return False
        except Exception as e :
            print(f"Failed with {e}")
            return False