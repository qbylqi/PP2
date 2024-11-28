import psycopg2

# Подключение к базе данных
connection = psycopg2.connect(
    host="localhost",
    dbname="snake_game_db",  # База данных должна быть уже создана
    user="postgres",
    password="Islandrich@",
    port="5432"
)
cur = connection.cursor()

# Создание таблиц, если они не существуют
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    username VARCHAR(255) PRIMARY KEY
);
""")
cur.execute("""
CREATE TABLE IF NOT EXISTS user_score (
    user_score INT NOT NULL,
    user_level INT NOT NULL,
    username VARCHAR(255) NOT NULL,
    FOREIGN KEY (username) REFERENCES users(username)
);
""")

# Сохранение изменений и закрытие соединения
connection.commit()
cur.close()
connection.close()

print("Таблицы успешно созданы!")
