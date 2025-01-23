todos = []
todos.append("Go To Program")
todos.append("Learn AI App work")
todos.append("learn to make todo")
print(todos)

total_todo = int(input("Enter how many list you want: "))

for i in range (1,total_todo+1):
    item = input(f" Enter todo list{i}: ")
    todos.append(item)

print("\n All todo are:  ")
for i in range(0, len(todos)):
    print(todos[i])