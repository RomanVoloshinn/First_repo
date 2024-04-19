
import pickle

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()  # Повертаємо новий екземпляр, якщо файл не знайдено



def main():
    book = load_data()  # Завантаження адресної книги з файлу при старті програми

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = user_input.split()
        if command in ["close", "exit"]:
            print("Good bye!")
            save_data(book)  # Збереження адресної книги в файл перед виходом з програми
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
