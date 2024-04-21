from datetime import datetime, timedelta
import re
import pickle

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

# Классы для обработки данных о дате рождения, телефонном номере и записи контакта
class Birthday(Field):
    def __init__(self, value):
        try:
            super().__init__(datetime.strptime(value, "%d.%m.%Y"))
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

class Record:
    def __init__(self, name):
        self.name = name
        self.phones = []
        self.birthday = None

    def add_birthday(self, value):
        self.birthday = Birthday(value)

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def __str__(self):
        phones_info = ", ".join([str(phone) for phone in self.phones])
        return f"Name: {self.name} Birthday: {self.birthday} Phones: {phones_info}"

class Phone(Field):
    def __init__(self, value):
        if not re.match(r'^\+?\d{1,3}?\s?\(?(?:\d{2,3})\)?(?:[-.\s]?\d{2,3}){2,3}$', value):
            raise ValueError("Invalid phone number format.")
        super().__init__(value)

    def __str__(self):
        return str(self.value)

# Класс для управления записями контактов
class AddressBook:
    def __init__(self):
        self.records = dict()

    def add_record(self, record):
        self.records.update({record.name : record})

    def find(self, name):
        return self.records.get(name)

    def get_upcoming_birthdays(self):
        today = datetime.today().date()
        upcoming_birthdays = []

        for record in self.records.values():
            if record.birthday:
                birthday = record.birthday.value
                birthday = birthday.replace(year=today.year).date()
                if birthday < today:
                    birthday = birthday.replace(year=today.year + 1)

                days_until_birthday = (birthday - today).days

                if 0 <= days_until_birthday <= 6:
                    if birthday.weekday() >= 5:
                        weekday_difference = 7 - birthday.weekday()
                        birthday += timedelta(days=weekday_difference)

                    upcoming_birthdays.append({
                        "name": record.name,
                        "congratulation_date": birthday.strftime("%Y.%m.%d")
                    })

        return upcoming_birthdays

# Функция для обработки ошибок ввода команд
def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return f"Error: {str(e)}"
    return wrapper

# Функции обработки команд
@input_error
def add_birthday(args, book):
    name, birthday = args
    record = book.find(name)
    if record:
        record.add_birthday(birthday)
        return f"Birthday added for {name}."
    else:
        return "Contact not found."

@input_error
def show_birthday(args, book):
    name, *_ = args
    record = book.find(name)
    if record and record.birthday:
        return f"{name}'s birthday: {record.birthday.value.strftime('%d.%m.%Y')}"
    elif record:
        return f"{name} has no birthday set."
    else:
        return "Contact not found."

@input_error
def birthdays(book):
    upcoming_birthdays = book.get_upcoming_birthdays()
    if upcoming_birthdays:
        return "\n".join([f"{entry['name']}'s birthday is on {entry['congratulation_date']}" for entry in upcoming_birthdays])
    else:
        return "No upcoming birthdays."

def main():
    book = load_data()

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = user_input.split()
        if command in ["close", "exit"]:
            print("Good bye!")
            save_data(book)
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            if len(args) != 2:
                print("Usage: add [name] [phone]")
                continue
            name, phone = args
            record = book.find(name)
            if record:
                record.add_phone(phone)
                print(f"Added phone {phone} to {name}")
            else:
                record = Record(name)
                record.add_phone(phone)
                book.add_record(record)
                print(f"Added new contact {name} with phone {phone}")
        elif command == "change":
            if len(args) != 2:
                print("Usage: change [name] [new phone]")
                continue
            name, new_phone = args
            record = book.find(name)
            if record:
                record.phones = [new_phone]
                print(f"Changed phone for {name} to {new_phone}")
            else:
                print(f"Contact {name} not found")
        elif command == "phone":
            if len(args) != 1:
                print("Usage: phone [name]")
                continue
            name = args[0]
            record = book.find(name)
            if record:
                print(f"Phone for {name}: {record.phones}")
            else:
                print(f"Contact {name} not found")
        elif command == "all":
            print("All contacts:")
            for name, record in book.records.items():
                print(record)
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(birthdays(book))
        else:
            print("Invalid command.")

if __name__ == '__main__':
    main()