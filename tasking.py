from datetime import datetime, timedelta
import time


class Task:

    def __init__(self):
        self.tasks = []

    def add_task(self, task_name, expire, state):
        for task in self.tasks:
            if task['task_name'] == task_name:
                task['expire'] = expire
                task['state'] = state
                print(f'Задача "{task_name}" обновлена')
                return
        new_task = {
            'task_name': task_name,
            'expire': expire,
            'state': state
        }
        self.tasks.append(new_task)
        print(f'Задача "{task_name}" добавлена')

    def expire_not_executed_task(self):
        not_performed_task = [task['task_name'] for task in self.tasks if task['state'] and
                          datetime.now() > task['expire']]
        if not_performed_task:
            print(f'Задача(и) "{", ".join(not_performed_task)}" не выполнен(а)ы в срок')

    def executed_task(self):
        performed_task = [task['task_name'] for task in self.tasks if task['state'] == False]
        if performed_task:
            print(f'Задач(а)и "{", ".join(performed_task)}" выполнен(а)ы в срок')

    def show_perfoming_tasks(self):
        performing_task = [
            task['task_name'] for task in self.tasks
            if 'state' in task and task['state'] == True and datetime.now() <= task['expire']
        ]
        if performing_task:
            print(f'Задача(и) "{", ".join(performing_task)}" все еще выполняются')


    def show_info(self):
        for task in self.tasks:
            status = 'выполняется' if task['state'] == True else 'завершена'
            print(f'Задача -- "{task['task_name']}"\n'
                  f'Срок выполнения -- "{task['expire'].strftime("%Y-%m-%d %H:%M:%S")}"'
                  f'\nСтатус -- "{status}"')


task1_expire_time = datetime.now() + timedelta(seconds=10)
first_task = Task()
first_task.add_task("порешать задачи на Python", task1_expire_time, True)
print(first_task.show_info())
print('-------------------------------------------------------')

time.sleep(11)
print(first_task.expire_not_executed_task())
print('-------------------------------------------------------')

time.sleep(2)
task2_expire_time = datetime.now() + timedelta(minutes=10)
first_task.add_task("порешать задачи на C#", task2_expire_time, True)
print(first_task.show_info())
print('-------------------------------------------------------')

time.sleep(3)
first_task.add_task("порешать задачи на C#", task2_expire_time, False)
print(first_task.show_info())
print('-------------------------------------------------------')

time.sleep(3)
task3_expire_time = datetime.now() + timedelta(minutes=5)
first_task.add_task("порешать задачи на Java", task2_expire_time, True)
print(first_task.show_info())
print('-------------------------------------------------------')

time.sleep(3)
first_task.add_task("порешать задачи на Java", task2_expire_time, False)
task4_expire_time = datetime.now() + timedelta(minutes=5)
first_task.add_task("порешать задачи на Delphi", task4_expire_time, True)
print(first_task.show_info())
print('-------------------------------------------------------')

print(first_task.executed_task())
print(first_task.expire_not_executed_task())
print(first_task.show_perfoming_tasks())
print('-------------------------------------------------------')
