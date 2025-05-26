import psycopg2
from psycopg2 import OperationalError

def create_connection():
    conn = None
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="game_tracker",
            user="game_user",
            password="1234"
        )
        print("Подключение к PostgreSQL успешно!")
        return conn
    except OperationalError as e:
        print(f"Ошибка подключения: {e}")
    return conn

def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS games (
                id SERIAL PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                rating DECIMAL(3, 1) CHECK (rating >= 1 AND rating <= 5),
                completion_time DECIMAL(6, 2)
            )
        """)
        conn.commit()
        print("Таблица 'games' создана или уже существует.")
    except OperationalError as e:
        print(f"Ошибка создания таблицы: {e}")