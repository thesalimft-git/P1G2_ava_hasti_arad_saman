
Tasks = [
    {'title': 'buy food', 'status': 'pending'},
    {'title': 'call mom', 'status': 'pending'}
]

# Tasks = []



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
    Tasks.append({
        'title': task,
        'status': 'pending'
    })
    print('successful')
    
def delete_task():
    show_task()
    task_id = int(input('which task to delete: '))
    if task_id > 0 and task_id < len(Tasks):
        Tasks[task_id - 1]['status'] = 'deleted'

def complete_task():
    show_task()
    task_id = int(input('which task to complete: '))
    if task_id > 0 and task_id < len(Tasks):
        Tasks[task_id - 1]['status'] = 'completed'
        # Tasks[task_id - 1].update({'status': 'completed'})
        

def show_task():
    for task in Tasks:
        if task.get('status') != 'deleted': 
            print(f'{task.get('title')} ({task.get('status')})')
    
    # 1- buy food
    # 2- call mom (completed)


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
                break
            case _:
                print('invalid command')
                    
        
            

main()