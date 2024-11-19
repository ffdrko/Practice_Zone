todo_list = []

while True:
    user_action = input("Type add, show or exit: ").strip()

    match user_action:
        case 'add':
            todo_task = input("Enter your task: ")
            todo_list.append(todo_task)
        case 'show'| 'display':
            for task in todo_list:
                print(task)
        case 'exit':
            break
        case whatever:
            print("wrong action...")

print('Bye')