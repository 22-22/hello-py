HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи."""

tasks = []
today = list() # today = []
tomorrow = list()
other = list()

run = True

while run:
    command = input("Введите команду\n")
    if command == "help":
        print(HELP)
    elif command == "show":
        print(tasks)
        print("Сегодня")
        for task in today:
            print(task)
    elif command == "add":
        task = input("Введите название задачи: ")
        date = input("Когда выполнить задание? ")
        tasks.append(task)
        if date == "Сегодня":
            today.append(task)
        elif date == "Завтра":
            tomorrow.append(task)
        else:
            other.append(task)
        print(f"Задача {task} добавлена")
    elif command == "exit":
        print("Спасибо за использование! До свидания!")
        break
    else:
        print("Неизвестная команда")
        break

print("До свидания!")