def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Помилка: Контакт не знайдено."
        except ValueError:
            return "Помилка: Введіть ім'я та телефон."
        except IndexError:
            return "Помилка: Недостатньо аргументів."

    return inner

def parse_input(user_input):
    if user_input:
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, args
    else:
        return None, []

@input_error
def add_contact(args, contacts):
    if len(args) >= 2:
        name, phone = args
        contacts[name] = phone
        return "Контакт додано."
    else:
        raise ValueError

@input_error
def change_contact(args, contacts):
    if len(args) >= 2:
        name, new_phone = args
        if name in contacts:
            contacts[name] = new_phone
            return f"Номер телефону для '{name}' змінено."
        else:
            raise KeyError
    else:
        raise IndexError

@input_error
def get_phone(args, contacts):
    if args:
        name = args[0]
        if name in contacts:
            return f"Номер телефону для '{name}' - {contacts[name]}."
        else:
            raise KeyError
    else:
        raise ValueError

def display_all_contacts(contacts):
    if contacts:
        all_contacts = "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
        return f"Усі контакти:\n{all_contacts}"
    else:
        return "Контакти відсутні."

def main():
    contacts = {}
    print("Ласкаво просимо до асистента!")
    while True:
        user_input = input("Введіть команду: ")
        command, args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("До побачення!")
            break
        elif command == "hello":
            print("Як я можу вам допомогти?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_phone(args, contacts))
        elif command == "all":
            print(display_all_contacts(contacts))
        else:
            print("Невірна команда.")

if __name__ == "__main__":
    main()