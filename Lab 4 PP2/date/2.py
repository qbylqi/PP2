from datetime import datetime, timedelta

# Текущая дата
today = datetime.now()

# Вчера
yesterday = today - timedelta(days=1)

# Завтра
tomorrow = today + timedelta(days=1)

print("Вчера:", yesterday.date())
print("Сегодня:", today.date())
print("Завтра:", tomorrow.date())
