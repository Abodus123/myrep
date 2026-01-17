print('Приветствую всех')
tasks = []
def see_tasks():
    if not tasks:
        print('Задач нету')
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")