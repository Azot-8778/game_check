import psycopg2
from database import create_connection, create_table


def print_menu():
    print("\n=== Меню ===")
    print("1. Добавить игру")
    print("2. Показать все игры")
    print("4. Удалить игру")
    print("5. Выход")


def add_game(conn):
    title = input("Название игры: ")
    rating = float(input("Оценка (1-5): "))
    completion_time = float(input("Время прохождения (часы): "))

    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO games (title, rating, completion_time) VALUES (%s, %s, %s) RETURNING id",
        (title, rating, completion_time)
    )
    game_id = cursor.fetchone()[0]
    conn.commit()
    print(f"Игра '{title}' (ID: {game_id}) добавлена!")


def show_games(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM games")
    games = cursor.fetchall()

    if not games:
        print("Список игр пуст.")
    else:
        print("\nСписок игр:")
        for game in games:
            print(f"ID: {game[0]}, Название: {game[1]}, Оценка: {game[2]}, Время: {game[3]} ч.")




def delete_game(conn):
    show_games(conn)
    game_id = int(input("Введите ID игры для удаления: "))

    cursor = conn.cursor()
    cursor.execute("DELETE FROM games WHERE id = ?", (game_id,))
    conn.commit()
    print("Игра удалена!")


def main():
    conn = create_connection()
    if conn:
        create_table(conn)

        while True:
            print_menu()
            choice = input("Выберите действие: ")

            if choice == "1":
                add_game(conn)
            elif choice == "2":
                show_games(conn)
            elif choice == "4":
                delete_game(conn)
            elif choice == "5":
                print("Выход...")
                break
            else:
                print("Неверный ввод!")

        conn.close()


if __name__ == "__main__":
    main()