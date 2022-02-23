import random

# dict().keys() -> Список ключей
# dict().values() -> Список значений
# value in dict().values()

HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи."""
# RANDOM_TASK = "Посмотреть кино"
RANDOM_TASKS =  ['Написать Гвидо письмо', 'Выучить Python', 
'Записаться на курс в Нетологию', 'Посмотреть 4 сезон Рик и Морти']
tasks = {}
run = True

def add_todo(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = [task]
    print(f"Задача {task} добавлена на дату {date}")

while run:
    command = input("Введите команду\n")
    command = command.lower()
    if command == "help":
        print(HELP)
    elif command == "show":
        date = input("Какую дату вы хотите посмотреть? ")
        if date in tasks:
            for task in tasks[date]:
                print("-", task)
        else:
            print("Такой даты нет")
    elif command == "add":
        task = input("Введите название задачи: ")
        date = input("Когда выполнить задание? ")
        add_todo(date, task)
    elif command == "random":
        # add_todo("Сегодня", RANDOM_TASK)
        task = random.choice(RANDOM_TASKS)
        add_todo("Сегодня", task)
    elif command == "exit":
        print("Спасибо за использование! До свидания!")
        break
    else:
        print("Неизвестная команда")
        break

print("До свидания!")