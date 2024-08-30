task1=input("Enter the task ")
task2=input("Enter the task ")
task3=input("Enter the task ")
tasks=[task1,task2,task3]
def show():
    for i in tasks:
     print("The tasks are ",i)
def delete():
    Del_task=input("Enter the task you want to delete").lower()
    if Del_task in tasks:
        tasks.remove(Del_task)
show()
delete()        
print("New list is")
show()       