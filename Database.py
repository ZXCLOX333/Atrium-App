import pyodbc

class DatabaseManager:
    def __init__(self):
        self.conn_str = (
            "Driver={SQL Server};" 
            "Server=DESKTOP-5TIDMAG\SQLEXPRESS;"  
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
        
if __name__ == "__main__":
    db = DatabaseManager()
    print("Тестуємо підключення...")
    try:
        movies = db.get_movies()
        print(f"Підключення успішне. Знайдено фільмів: {len(movies)}")
    except Exception as e:
        print(f"Підключення не вдалося: {e}")