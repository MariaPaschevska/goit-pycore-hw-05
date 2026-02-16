# Це простий бот-асистент, який може обробляти базові команди для керування контактами
from functools import wraps

# Розбираємо вхідні дані на команду та аргументи
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

# Декоратор для обробки помилок введення
def input_error(func):
    # Використовуємо wraps для збереження метаданих оригінальної функції
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        
        except KeyError:
            return "Contact not found."
        
        except IndexError:
            return "Give me name and phone please."

    return inner

# Команда для додавання контакту: "add <name> <phone>"
@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

# Команда для зміни номера контакту: "change <name> <new_phone>"
@input_error
def change_contact(args, contacts):
    name, phone = args  
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Contact updated."

# Команда для виведення номера зазначеного контакту: "phone <name>"
@input_error
def get_phone(args, contacts):
    name = args[0] 
    return f"{name}'s phone number: {contacts[name]}"

# Команда для виведення усіх контактів
@input_error
def list_contacts(contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change": 
            print(change_contact(args, contacts))
        elif command == "all":
            print(list_contacts(contacts))
        elif command == "phone":
            print(get_phone(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
