while True:
    user_Action = input("Type add, show, edit, complete, exit: ").strip()

    match user_Action:
        case 'add':
            file = open("File/todo_list.txt", 'r')
            todo_list = file.readlines()

            todo = input("Enter a todo: ")+ '\n'
            todo_list.append(todo)

            file = open("File/todo_list.txt", 'w')
            file.writelines(todo_list)
        case 'show':
            for index, item in enumerate(todo_list):
                print(f"{index + 1} - {item}")
        case 'exit':
            break
