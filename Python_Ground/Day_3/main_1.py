todo_list = []

while True:
    user_action = input("Type add or show or exit: ")

    match user_action:
        case 'add':
            todo_task = input("Enter a todo: ")
            todo_list.append(todo_task)
        case 'show':
            print(todo_list)
        case "exit":
            break

print('Bye')