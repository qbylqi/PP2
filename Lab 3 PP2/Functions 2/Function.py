# Список фильмов
movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]

# 1. Функция, которая проверяет, больше ли рейтинг фильма 5.5
def is_high_score(movie):
    return movie['imdb'] > 5.5

# Пример использования
print(is_high_score(movies[0]))  # True

# 2. Функция, которая возвращает подсписок фильмов с рейтингом выше 5.5
def get_high_score_movies(movies):
    return [movie for movie in movies if movie['imdb'] > 5.5]

# Пример использования
print(get_high_score_movies(movies))

# 3. Функция, которая возвращает фильмы по категории
def get_movies_by_category(movies, category):
    return [movie for movie in movies if movie['category'] == category]

# Пример использования
print(get_movies_by_category(movies, "Romance"))

# 4. Функция, которая вычисляет средний рейтинг по списку фильмов
def calculate_average_imdb(movies):
    total_imdb = sum(movie['imdb'] for movie in movies)
    return total_imdb / len(movies) if movies else 0

# Пример использования
print(calculate_average_imdb(movies))

# 5. Функция, которая вычисляет средний рейтинг по категории
def calculate_average_imdb_by_category(movies, category):
    category_movies = [movie for movie in movies if movie['category'] == category]
    return calculate_average_imdb(category_movies)

# Пример использования
print(calculate_average_imdb_by_category(movies, "Romance"))
