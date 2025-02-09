import sqlite3

class AccessDB:
    def __init__(self,db_path):
        try:
            self.conn = sqlite3.connect(db_path)  
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e : 
            raise RuntimeError(f"Database error connetion: {e}")
        
    
    def get_user_info(self,email) ->tuple:
        query = "SELECT email,password FROM user_data WHERE email = (?)"
        self.cursor.execute(query, (email,))
        userPresent = self.cursor.fetchone()
        return userPresent if userPresent else None


    def add_new_user(self,email,password) ->bool:
        userData=[(email,password)]
        try:
            query = '''INSERT INTO user_data (email, password) VALUES (?, ?)'''
            self.cursor.executemany(query, userData)
            self.conn.commit()
            return True
        except:
            return False

    def close_connection(self):
        self.cursor.close()
        self.conn.close()

        pass    
    
        
