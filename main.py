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