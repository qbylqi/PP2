from datetime import datetime, timedelta

# Текущая дата и время
current_date = datetime.now()

# Вычитаем 5 дней
new_date = current_date - timedelta(days=5)

print("Текущая дата:", current_date)
print("Дата пять дней назад:", new_date)
