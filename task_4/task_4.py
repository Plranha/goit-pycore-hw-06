def parse_input(user_input):
    parts = user_input.split()
    if not parts:
        return "", []
    cmd = parts[0].lower()
    args = parts[1:]
    return cmd, args

def add_contact(args, contacts):
    if len(args) != 2:
         return "Errir: Please provodi name and phone number"
    name, phone = args
    contacts[name] = phone
    return "Contact added"

def change_contact(args, contacts):
     if len(args) !=2:
         return "Error: Please provide name and new phone number"
     name, new_phone = args
     if name not in contacts:
         return f"Error: Contact {name} not found"
     contacts[name] = new_phone
     return "Contact updated"


def show_phone(args,contacts):
    if len(args) != 1:
        return "Error: Please provide name"
    name = args[0]
    if name not in contacts:
        return f"Error: Contact {name} not found"
    return contacts[name]


def show_all(contacts):
    if not contacts:
        return "No contact found"
    
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)
   

def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input('Enter a command: ').strip()
        command, args = parse_input(user_input)
        
        if command in ["close",'exit']:
            print('Good bye!')
            break
        elif command == 'hello' or command == 'hi':
            print('How can I help you?')
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print('Invalid command')
    
    
if __name__ == '__main__':
    main()