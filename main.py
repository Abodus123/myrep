print('Приветствую всех')
tasks = []
def see_tasks():
    if not tasks:
        print('Задач нету')
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def del_task(number_task):
    if 0 < number_task < len(tasks):
        tasks.pop(number_task - 1)
        print('задача удалена')
    else:
        print('Такой задачи не сущетствует')



def task_add(new_task):
    tasks.append(new_task)
    print('Задача добавленна')

while True:
    answer = int(input('Выберите действие. 1- показать, 2 -добавить, 3 - выйти, 4 - удалить'))
    if answer == 1:
        see_tasks()
    elif answer == 2:
        new_task = input('Введите новую задачу')
        task_add(new_task)
    elif answer == 3:
        break
    elif answer == 4:
        number_task = int(input('Введите номер задачи'))
        del_task(number_task)
    else:
        print('Вы ввели не правильную цифру')
