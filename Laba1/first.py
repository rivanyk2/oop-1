from datetime import date

# Отримати поточну дату
today = date.today()
month = today.month

# Визначення пори року за місяцем
if month in [12, 1, 2]:
    season = "Зима"
elif month in [3, 4, 5]:
    season = "Весна"
elif month in [6, 7, 8]:
    season = "Літо"
else:
    season = "Осінь"

# Вивід результатів
print(f"Місяць: {today.strftime('%B')}, Пора року: {season}")
