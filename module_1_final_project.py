# Create a tasks list
tasks = []

# Function to add tasks
def add_task(): 
    task= input("Enter a new task: ")
    tasks.append(task)
    print(f"Task {task} added sucessfully.")
    
# Function to view tasks 
def list_tasks():
    if not tasks:
      print("There are no tasks at this time.")
    else:
      print("Current Tasks: ")
      print("-----------------------------------------------------------------------------------------")
      for index, task in enumerate(tasks, 1):
        print(f"Task #{index}. {task}")
       
    
# Function for deleting tasks
def delete_task():
    list_tasks()
    try:
        task_to_delete = int(input("Enter the number you would like to delete: "))
        if task_to_delete >= 0 and task_to_delete < len (tasks):
          tasks.pop(task_to_delete-1)    
          print(f"Task {task_to_delete} has been successfuly deleted.")
        else: 
          print(f"Task {task_to_delete} was not found. Try again. ")
    except:
       print("Invalid answer.")
       
# Function to display options and create loop          
def main():

    while True: 
     print("\nWelcome to the to do list app!")
     print("Please select one of the following options:")
     print("1. Add a new task")
     print("2. Delete a task")
     print("3. List tasks")
     print("4. Quit app")
        
     choice = input("Please enter your choice (1-4): ")
     
     if(choice == "1"):
        add_task ()
     elif(choice == "2"):
        delete_task() 
     elif(choice == "3"):
        list_tasks()
     elif(choice == "4"):
         break
     else: 
         print("Invalid answer. Please Try again.")
         print("Goodbye!")
main()
            
            
      