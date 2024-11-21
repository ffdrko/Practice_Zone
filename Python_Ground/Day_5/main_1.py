todo_list = []

while True:
    user_action = input("Type add, show, edit or exit: ").strip()

    match user_action:
        case "add":
            task = input("Enter a todo: ")
            todo_list.append(task)
        case 'show':
            for index, item in enumerate(todo_list):
                print(index, "-", item)
        case "edit":
            todo_num = int(input("Enter todo number:  ")) - 1
            todo_list[todo_num] = input("Enter new todo: ")
        case "exit":
            break

print("Bye...")