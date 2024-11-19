todo_list = []

while True:
    user_action = input("Type add, show or exit: ").strip()

    match user_action:
        case 'add':
            todo_task = input("Enter your task: ")
            todo_list.append(todo_task)
        case 'show':
            for task in todo_list:
                print(task)
        case 'exit':
            break

print('Bye')