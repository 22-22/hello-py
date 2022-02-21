#Задание 1
date = input("Введите дату: ")
task = input("Введите задачу: ")
print(date, task)

#Задание 2
list = []
for x in range(3):
    date = input("Введите дату: ")
    task = input("Введите задачу: ")
    list.append(date + " " + task)
print(list[0] + "\n" + list[1] + "\n" + list[2])

#Задание 3
dict = {}
for x in range(3):
    date = input("Введите дату: ")
    task = input("Введите задачу: ")
    dict[date] = task
print(dict)

