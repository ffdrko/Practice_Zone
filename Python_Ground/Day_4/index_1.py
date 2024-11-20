todo_list = []

while True:
    user_action = input("Type add, show, edit or exit:  ").strip()

    match user_action:
        case 'add':
            task = input("Enter a todo: ")
            todo_list.append(task)

        case 'show':
            for task in todo_list:
                print(task)

        case 'edit':
            task_num = int(input("Enter the serial number task to edit: "))
            todo_list[task_num - 1] = input("Enter new todo: ")

        case 'exit':
            break


print("Bye...")