user_prompt = "Enter a todo: "
todo_list = []

while True:
    todo_task = input(user_prompt)
    todo_list.append(todo_task)
    print(todo_task.title())
    print(todo_task.capitalize())