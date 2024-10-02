from datetime import datetime

# Текущая дата и время с микросекундами
current_datetime = datetime.now()

# Удаление микросекунд
new_datetime = current_datetime.replace(microsecond=0)

print("Текущая дата и время:", current_datetime)
print("Без микросекунд:", new_datetime)
