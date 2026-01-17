print('Приветствую всех')
tasks = []
def see_tasks():
    if not tasks:
        print('Задач нету')
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def task_add(new_task):
    tasks.append(new_task)
    print('Задача добавленна')

while True:
    answer = int(input('Выберите действие. 1- показать, 2 -добавить, 0 - выйти'))
    if answer == 1:
        see_tasks()
    elif answer == 2:
        new_task = input('Введите новую задачу')
        task_add(new_task)
    elif answer == 3:
        break
    else:
        print('Вы ввели не правильную цифру')
