#Create program that ask usert to enter n no of to do and display it
todos =[]

total_todo = int (input("Enter total no of todo: "))

for i in range(1,total_todo+1):
    todo = input(f"Enter todo {i}: ")
    todos.append(todo)


print("\n------\n")
print ("All todos are: ")

    #Display all result
for todo in todos:
  print(todo)