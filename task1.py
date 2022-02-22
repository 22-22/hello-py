HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи."""

tasks = []
today = []
tomorrow = []
other = []

run = True

while run:
    command = input("Введите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        print(tasks, today, tomorrow, other)
    elif command == "add":
        task = input("Введите название задачи: ")
        date = input("Когда выполнить задание? ")
        tasks.append(task)
        if date == "Сегодня":
            today.append(date)
        elif date == "Завтра":
            tomorrow.append(date)
        else:
            other.append(date)
        print("Задача добавлена")
    elif command == "exit":
        print("Спасибо за использование! До свидания!")
        break
    else:
        print("Неизвестная команда")
        break

print("До свидания!")