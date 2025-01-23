# storing multiple value in same variable 
names = ["roshan", "rojay", "shyam"]
names.append("Martin")
print(names)
print(len(names))
names.remove("rojay")
print(len(names)) #prints length
print(names[0])
print(names[1])
print(names[2])
reverse_name = names[::-1]
print(reverse_name)

#Monthly expances taraker using list

monthly_expenses = [20, 30, 40]
monthly_expenses.append(50)
reverse_list = monthly_expenses.reverse()
total_spend = sum(monthly_expenses)
print(f"Total monthly expences: ", total_spend)
print(max(monthly_expenses)) #prints maximum number
print(min(monthly_expenses)) #prints minimum number

# CREATE A EMPTY ;IST OF TYPW STRINGS CALLED DAYS.  USE THE ADD METHOD TO ADD NAMES OF 7 DAYS AND PRINT ALL DAYS 
days = []
days.append("Monday")
days.append("Tuesday")
days.append("Wednesday")
days.append("Thursday")
days.append("Friday")
days.append("Saturday")
print(f"The number of days are: {days}")
for day in (days):
    print(f"days are: {day}")

# Use where to find a day name that start with the alphabed "T"
days_starting_with_t = [day for day in days if day.startswith("T") or day.startswith("S")]
print(days_starting_with_t)
# for day in days:
#     if day.startswith("T"):
#         print(day)  


#List comprehension in python
# new_list = [expression for item in iterable if condition]

numbers= [1,2,3,4,5,6,7,8,9,10]
squares = [x**2 for x in numbers]
print(squares)

cubes =[x**3 for x in range(1,6)]
print(cubes)

even_num = [num for num in range(1,20) if num % 2 == 0]
print(even_num)

words = ["apple", "banana", "cherry", "te", "elderberry"]
long_word_upper = [words.capitalize() for words in words if len(words)>4]
print(long_word_upper)