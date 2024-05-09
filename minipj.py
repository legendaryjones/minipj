#to do list project

#create a empty list for user input
# to do list function
#menu options and user choice

to_do_list = []

def print_to_do_list (to_do_list):
   print("Current to do list:")
   for task in to_do_list:
    print (f"{task}")
    

print('''
      
    Welcome to Mikes To-Do List
    Menu
    1. Add a task
    2. View tasks
    3. Mark a task as complete
    4. Delete a task
    5. Quit''') 

while True:
        action = input ("Please select an option from the menu:")
        if not action in  ['1', '2', '3', '4', '5', ]: 
            print ( 'Please enter one numerical response of 1-5')
        elif action == '1': 
         task= input ("Enter the item you want to add:")
         to_do_list.append(task)
         print (f'{task} has been added to your to do list')
        elif action == '2': 
            print_to_do_list(to_do_list)
        elif action == '3': 
             task = input(f'which task in your to do list {to_do_list} have you finished?')
             input (f'{task} is now complete')
        elif task not in to_do_list:
         print (f"{task} is not in your to_do_list")
        elif action == '4': 
            task = input('Enter the task you want to delete')
            if task in to_do_list:
                to_do_list.remove(task)
            (f'{task} has been removed')
        elif action == '4':
            task = input
            if task not in to_do_list:
                (f'{task} is not in your to do list')
        elif action == '5':
            task = input('Quitting list until later')
            break
  