import pyodbc

class DatabaseManager:
    def __init__(self):
        self.conn_str = (
            "Driver={SQL Server};" 
            "Server=DESKTOP-5TIDMAG\\SQLEXPRESS;" 
            "Database=AtriumDB;"
            "Trusted_Connection=yes;"
        )

    def login(self, email, password):
        try:
            conn = pyodbc.connect(self.conn_str)
            cursor = conn.cursor()

            cursor.execute("SELECT UserID, FullName, Password FROM Users WHERE Email = ?", (email,))
            user = cursor.fetchone()
            conn.close()
            
            if user:
                db_pass = user[2]
                
                if db_pass == password:
                    return {"id": user[0], "name": user[1]}
            
            return None
        except Exception as e:
            print(f"Помилка бази даних: {e}")
            return None
        
    def get_all_movies(self):
        try:
            conn = pyodbc.connect(self.conn_str)
            cursor = conn.cursor()
            query = "SELECT Title, ImageFileName, Price, Description FROM Movies"
            cursor.execute(query)
            movies = cursor.fetchall()
            conn.close()
            return movies
        except Exception as e:
            print(f"Помилка отримання всіх фільмів: {e}")
            return []
        
    def get_movies(self, title):
        try:
            conn = pyodbc.connect(self.conn_str)
            cursor = conn.cursor()
            query = "SELECT Title, ImageFileName, Price, Description FROM Movies WHERE Title LIKE ?"
            cursor.execute(query, (f"%{title}%",))
            
            movie = cursor.fetchone()
            conn.close()
            return movie
        except Exception as e:
            print(f"Помилка: {e}")
            return None 
        
    def register_user(self, fullname, email, password):
        try:
            conn = pyodbc.connect(self.conn_str)
            cursor = conn.cursor()
            query = "INSERT INTO Users (FullName, Email, Password) VALUES (?, ?, ?)"
            cursor.execute(query,(fullname, email, password))
            conn.commit()
            conn.close()
            return True, "Succes"
        except pyodbc.IntegrityError:
            return False, "Email already registered."
        except pyodbc.Error as e:
            print(f"SQL Error: {e}")
            return False, "Password doesn`t meet requirements (Need: A-Z, 0-9, special char)."
        except Exception as e:
            return False, str(e)
        
    def check_email_exists(self, email):
        try:
            conn = pyodbc.connect(self.conn_str)
            cursor = conn.cursor()
            cursor.execute("SELECT UserID FROM Users WHERE Email = ?", (email,))
            result = cursor.fetchone()
            conn.close()
            return result is not None
        except:
            return False


    def update_password(self, email, new_password):
        try:
            conn = pyodbc.connect(self.conn_str)
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE Users SET Password = ? WHERE Email = ?", 
                (new_password, email)
            )
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print("Password update error:", e)
            return False

if __name__ == "__main__":
    db = DatabaseManager()
    print("Тестуємо підключення...")
    try:
        movies = db.get_all_movies()
        print(f"Підключення успішне. Знайдено фільмів: {len(movies)}")
    except Exception as e:
        print(f"Підключення не вдалося: {e}")