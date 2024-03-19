# 1 exercise
def total_salary(path):
    total = 0
    count = 0
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    name, salary = line.strip().split(',')
                    total += int(salary)
                    count += 1
                except ValueError:
                    print(f"Помилка у рядку: {line}. Пропускаю цей рядок.")
    except FileNotFoundError:
        print("Файл не знайдено.")
        return None
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return None

    if count == 0:
        print("У файлі немає даних про зарплати розробників.")
        return None

    average_salary = int(total / count)
    return total, average_salary


path = "Salary.txt"
result = total_salary(path)
if result:
    total, average_salary = result
    print(f"Загальна сума зарплат: {total}")
    print(f"Середня зарплата: {average_salary}")

# 2 exercise

def get_cats_info(path):
    cats_list = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                try:
                    cat_id, name, age = line.strip().split(",")
                    cat_info = {
                        "id": cat_id,
                        "name": name,
                        "age": int(age)
                    }
                    cats_list.append(cat_info)
                except ValueError:
                    print(f"Помилка у рядку: {line}. Пропускаю цей рядок.")
    except FileNotFoundError:
        print("Файл не знайдено.")
        return None
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return None

    return cats_list


path = "cats.txt"
cats_info = get_cats_info(path)
if cats_info:
    for cat in cats_info:
        print(cat)

# 4 exercise

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
    name, phone = args[0], args[1]  # Змінив цей рядок
    contacts[name] = phone
    return "Контакт додано."

def change_contact(args, contacts):
    name, new_phone = args[0], args[1]  # Змінив цей рядок
    if name in contacts:
        contacts[name] = new_phone
        return f"Номер телефону для '{name}' змінено."
    else:
        return f"Контакт '{name}' не знайдено."

def get_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return f"Номер телефону для '{name}' - {contacts[name]}."
    else:
        return f"Контакт '{name}' не знайдено."

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