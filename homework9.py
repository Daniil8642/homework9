def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except (ValueError, IndexError):
            return "Give me name and phone please"

    return wrapper


class AssistantBot:
    def __init__(self):
        self.contacts = {}

    @input_error
    def add_contact(self, name, phone):
        self.contacts[name] = phone
        return f"Added {name} with phone number {phone}"

    @input_error
    def change_contact(self, name, phone):
        if name in self.contacts:
            self.contacts[name] = phone
            return f"Changed phone number for {name} to {phone}"
        else:
            return f"Contact {name} not found"

    @input_error
    def show_phone(self, name):
        if name in self.contacts:
            return f"{name}'s phone number is {self.contacts[name]}"
        else:
            return f"Contact {name} not found"

    def show_all(self):
        if not self.contacts:
            return "No contacts found"
        else:
            result = ""
            for name, phone in self.contacts.items():
                result += f"{name}: {phone}\n"
            return result

    def handle_command(self, command):
        command = command.lower()
        if command == "hello":
            return "How can I help you?"
        elif command.startswith("add "):
            parts = command.split(" ", 2)
            if len(parts) != 3:
                return "Invalid input format"
            name, phone = parts[1], parts[2]
            return self.add_contact(name, phone)
        elif command.startswith("change "):
            parts = command.split(" ", 2)
            if len(parts) != 3:
                return "Invalid input format"
            name, phone = parts[1], parts[2]
            return self.change_contact(name, phone)
        elif command.startswith("phone "):
            name = command.split(" ", 1)[1]
            return self.show_phone(name)
        elif command == "show all":
            return self.show_all()
        elif command in ("good bye", "close", "exit"):
            return "Good bye!"
        else:
            return "Unknown command"

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == ".":
                break
            response = self.handle_command(command)
            print(response)


if __name__ == "__main__":
    bot = AssistantBot()
    bot.run()



