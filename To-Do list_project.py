""" To-Do list project using python and oop concepts """


class Todo_list():
    def __init__(self):
        self.tasks = []


    def add_task(self,task):
        self.tasks.append({"task":task,"completed":False})
        print("Task added successfully...") 


    def remove_task(self,task):
        for t in self.tasks:
            if t["task"] == task:
                self.tasks.remove(t)
                print("Your task is removed succesfully...")
                return
            print("Task is not found....Check Again...")


    def mark_completed(self,task):
        for t in self.tasks:
            if t["task"] == task:
                t["completed"] = True
                print("Your task is completed...")
                return
            print("Task is not found....check again...")


    def display_task(self):
        if self.tasks:
            for i,t in enumerate(self.tasks,start=1):
                status = "completed" if t["completed"] else "Not Completed"
                print(f"{i}.{t['task']} - {status}")
        else:
            print("Your task is not in this list.....")


def main():
    todo_list = Todo_list()


    while True:
        print("\nTodolist menu..")
        print("1.ADD TASK")
        print("2.REMOVE TASK")
        print("3.MARK COMPLETED")
        print("4.DISPLAY TASKS")
        print("5.EXIT")


        choice = input("Enter your choice 1/2/3/4/5:")

        if choice == "1":
            task = input("Enter your task:")
            todo_list.add_task(task)

        elif choice == "2":
            task = input("Enter your removing task:")
            todo_list.remove_task(task)

        elif choice == "3":
            task = input("Enter your mark completed task:")
            todo_list.mark_completed(task) 


        elif choice == "4":
            todo_list.display_task()

        elif choice == "5":
            print("Exiting....")
            print("Todays List Done and Sucess")
            break

        else:
            print("Choose valid choice or Check ur option....")

main()                           

                        


                        


                       

