#1 Задание
from datetime import datetime

def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date, '%Y-%m-%d')

        current_date = datetime.today()

        date_difference = current_date - input_date

        return date_difference.days
    except ValueError:
        return


result = get_days_from_today('2022-03-06')
print(result)


#2 Задание
import random

def get_numbers_ticket(minimum, maximum, quantity):
    if not (1 <= minimum <= maximum <= 1000) or not (1 <= quantity <= maximum - minimum + 1):
        return []

    random_numbers = random.sample(range(minimum, maximum + 1), quantity)

    return sorted(random_numbers)

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)





#3 Задание
import re


def normalize_phone(phone_number):
    cleaned_number = re.sub(r'[^0-9+]', '', phone_number)

    if not cleaned_number.startswith('+'):
        if cleaned_number.startswith('380'):
            cleaned_number = '+' + cleaned_number
        else:
            cleaned_number = "+38" + cleaned_number

    return cleaned_number


phones = [
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "
]

for phone in phones:
    print(normalize_phone(phone))



#4 задание
from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date().replace(year=today.year )

        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)

        days_until_birthday = (birthday - today).days

        if 0 <= days_until_birthday <= 6:
            if birthday.weekday() >= 5:
                weekday_difference = 7 - birthday.weekday()
                birthday += timedelta(days=weekday_difference)

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": birthday.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays


users = [
    {"name": "Роман", "birthday": "2024.03.15"},
    {"name": "Анастасия", "birthday": "2024.03.10"},
]

result = get_upcoming_birthdays(users)
print(result)










