import sqlite3

class AccessDB:
    def __init__(self,db_path):
        self.conn = sqlite3.connect(db_path,check_same_thread=False)  
        self.cursor = self.conn.cursor()
        self.headers = ("id","email","password","admin")

    def __enter__(self):
        return self
    
    def __exit__(self,exc_type,exc_val,exc_rb):
        return self.close_connection()
        
    
    def get_user_info(self,email) ->dict | None:
        query = "SELECT * FROM user_data WHERE email = (?)"
        try:
            self.cursor.execute(query, (email,))
            userPresent = self.cursor.fetchone()
            return self._dict_from_row(userPresent) if userPresent else None
        except Exception as e:
            return None
        
    def _dict_from_row(self,row):
        return dict(zip(self.headers, row)) 


    def get_all_users(self)-> list[dict] | None:
        try:
            query = "SELECT * FROM user_data"
            self.cursor.execute(query)
            all_user_data = self.cursor.fetchall()
            return [self._dict_from_row(row) for row in all_user_data]
        except Exception as e :
            print(e)
            return None 
        

    def update_admin_status(self,user_id,stauts)->bool :
        try:
            query = "UPDATE user_data SET admin =? WHERE id = ?"
            self.cursor.execute(query,(stauts,user_id))
            self.conn.commit()
            return True
        except Exception as e :
            print(e)
            self.conn.rollback()
            return False


    def add_new_user(self,email,password) ->bool:
        self.cursor.execute("SELECT COUNT(*) FROM user_data")
        admin = 1 if self.cursor.fetchone()[0] == 0 else 0
        userData=[(email,password,admin)]
        try:
            query = '''INSERT INTO user_data (email, password,admin) VALUES (?,?,?)'''
            self.cursor.executemany(query, userData)
            self.conn.commit()
            return True
        except Exception as e :
            print(e)
            self.conn.rollback()
            return False
        

    def close_connection(self):
        if self.conn:  # Ensure connection exists
            print("Closing database connection")
            try:
                self.cursor.close()
                self.conn.close()
            except sqlite3.ProgrammingError:
                print("Database connection was already closed.")
    

    def update_user_email(self,new_email,id):
        user_data = (new_email,id)
        try:
            query = "UPDATE user_data SET email=? WHERE id = ?"
            self.cursor.execute(query,user_data)
            self.conn.commit()
            return True
        except Exception as e :
            print(e)
            self.conn.rollback()
            return False
        

    def update_user_password(self,new_password,id):
        user_data = (new_password,id)
        try:
            query = "UPDATE user_data SET password=? WHERE id = ?"
            self.cursor.execute(query,user_data)
            self.conn.commit()
            return True
        except Exception as e :
            print(e)
            self.conn.rollback()
            return False
