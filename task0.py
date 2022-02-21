#Задание 1
date = input("Введите дату: ")
task = input("Введите задачу: ")
print(date, task)

#Задание 2
my_list = []
for x in range(3):
    date = input("Введите дату: ")
    task = input("Введите задачу: ")
    my_list.append(date + " " + task)

for y in my_list:
    print(y)

#Задание 3
dict = {}
for x in range(3):
    date = input("Введите дату: ")
    task = input("Введите задачу: ")
    dict[date] = task
print(dict)

