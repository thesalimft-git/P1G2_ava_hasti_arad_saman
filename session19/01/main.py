import data_manager

try:
    Tasks = data_manager.get_data()
except:
    print('can not read the file')
    Tasks = []

def show_manu():
    print("\n--------------------------")
    print("1. View Task")
    print("2. Add Task")
    print("3. Mark Complete")
    print("4. Delete Task")
    print("5. Exit")
    print("\n")

def add_task():
    task = input("Enter a new task: ")
    if len(task) < 3:
        print('task must be at least 3 words')
    else:    
        Tasks.append({
            'title': task,
            'status': 'pending'
        })
        print('successful')
    
def delete_task():
    show_task()
    task_id = int(input('which task to delete: '))
    if task_id > 0 and task_id < len(Tasks):
        Tasks[task_id]['status'] = 'deleted'
    else:
        print('id is not valid')

def complete_task():
    if not Tasks:
        print('no task to complete')
        return
    
    show_task()
    try: 
        task_id = int(input('which task to complete: '))
    except:
        print('id is not valid, try again')
    
    # if task_id >= 0 and task_id < len(Tasks):
    if 0 <= task_id < len(Tasks):
        Tasks[task_id]['status'] = 'completed'
        # Tasks[task_id].update({'status': 'completed'})
        print(f'Task {task_id} is completed')
    else:
        print('id is not valid, try again')
               
def show_task():
    for index, task in enumerate(Tasks):
        if task.get('status') != 'deleted': 
            print(f'{index} - {task.get('title')} ({task.get('status')})')

def main():
    while True:
        show_manu()
        choice = input("Choose an option: ")
        match choice:
            case '1':
                show_task()
            case '2':
                add_task()
            case '3':
                complete_task()
            case '4':
                delete_task()
            case '5':
                data_manager.set_data(Tasks)
                break
            case _:
                print('invalid command')


main()