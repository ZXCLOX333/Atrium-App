import pyodbc

class DatabaseManager:
    def __init__(self):
        # Переконайтеся, що драйвер 'ODBC Driver 17 for SQL Server' встановлено
        self.conn_str = (
            "Driver={SQL Server};" 
            "Server=DESKTOP-JJ6476U\\SQLEXPRESS;"  # Подвійний слеш для Python
            "Database=AtriumDB;"
            "Trusted_Connection=yes;"
        )

    def login(self, email, password):
        try:
            conn = pyodbc.connect(self.conn_str)
            cursor = conn.cursor()
            
            # Використовуємо параметризовані запити для безпеки (проти SQL Injection)
            cursor.execute("SELECT UserID, FullName, Password FROM Users WHERE Email = ?", (email,))
            user = cursor.fetchone()
            conn.close()
            
            if user:
                # user[0]=ID, user[1]=Name, user[2]=Password
                db_pass = user[2]
                
                # Порівнюємо паролі
                if db_pass == password:
                    return {"id": user[0], "name": user[1]}
            
            return None
        except Exception as e:
            print(f"Помилка бази даних: {e}")
            return None

    def get_movies(self):
        try:
            conn = pyodbc.connect(self.conn_str)
            cursor = conn.cursor()
            cursor.execute("SELECT Title, ImageFileName, Price FROM Movies")
            movies = cursor.fetchall()
            conn.close()
            return movies
        except Exception as e:
            print(f"Помилка отримання фільмів: {e}")
            return []

if __name__ == "__main__":
    db = DatabaseManager()
    print("Тестуємо підключення...")
    try:
        movies = db.get_movies()
        print(f"Підключення успішне. Знайдено фільмів: {len(movies)}")
    except Exception as e:
        print(f"Підключення не вдалося: {e}")