from datetime import datetime

# Две даты
date1 = datetime(2024, 10, 1, 12, 0, 0)
date2 = datetime(2024, 10, 2, 12, 0, 0)

# Разница между датами в секундах
difference_in_seconds = (date2 - date1).total_seconds()

print("Разница в секундах:", difference_in_seconds)
