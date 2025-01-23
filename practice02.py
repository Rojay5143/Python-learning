#Condition in Python 
#checking Temparature 
temperature =30
if temperature > 25 :
    print(f"It's hot outside! where shorts and arms")
elif 15 <= temperature <= 25:
    print("It's a pleasent day! enjoy")
else:
    print("it's cold out side ")

#checking age for a movie tickets 

age = 2
if age <13:
    print("You are eligible for children tickets")
elif 13 <= age <= 59:
    print("your are eligible for adult Tickets")
else:
    print("Please Get yourself a senior Ticket")

# grade Evaluation 
score =  30 # this is to take input [input(f"Enter your Score: ")]
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >=70:
    grade = "C"
elif score >= 60:
    grade = "D"
elif score >=50:
    grade = "E"
else :
    grade = "F"
print(f"Your Grade is {grade} and score is {score}")


#assert in python 
price = 5 # if price is negative assert will stop the program 
assert price >= 0, "Price cannot be negative  " # it shows an error on the terminal if price is negative 
print("after price negative")

# LOOPS in python 
# first FOR loop 
# write a program to display your name 100 times 

for i in range( 10):
    print("My name is Rojay")

#display form  1 to 1000
for i in range(10, 0, -1): # inly range (100, 1 ) dosenot work because range function bcz the step is +1
    # sp 100 is greature than 1 so we have to expicity specify the negative valuw to counddown backwords 
    print(i)

# display even number between 1 to 1oo 
for j in range (1, 10):
    if j % 2 == 0:
        #print(f"the even number are:")
        print(j)
        
# LOOP over the name list 

names = ["Ram", "Shyam", "Hari", "krishna"]
for names in names:
    print(names)

#calculating the sum of numbers in list 

numbers =  [ 1,2,3,4,20]
total = 0 
for num in numbers:
    total += num 
print (total)

 #greeting for all friend using for loop 
friends = [ "Prashant", "Ankit", "Biswa"]
for friends in friends:
    print(f"Hello Mf {friends}")

# Accessing index and value with enumerator 

friends = [ "Prashant", "Ankit", "Biswa"]
for index, friends in enumerate(friends):
    print(f"Index : {index}, fridens: {friends}")

#while loop in python 
# while loop is used to execute a block of code as long as a given condition is true 
# Example  COUNTDOWN TIMER 

countdown = 5 
while countdown >0  :
    print(countdown)
    countdown -= 1
print("countdown complet")

count = 1
while count <= 10: #it keep running until count is less than or equal to 10 
    print(count) # it prient the current value of count
    count += 1 #it increment the value of count by 1 each time the loop runs

#create a password checker using while loop
password =""
while password != "Rojay123": #condition: Loop as long as password is correct
    password = input("enter your password: ")  #Prompt the user to enter a password
    if password != "Rojay123":
        print("Password is wrong. Please try again.")

print("Password is correct. Access granted.")
#-----------------------------------------------------------------------------------------------
#sum of the number until a condition is met using while loop
total = 0
number = int(input("Enter a number (0 to quit): ")) # Initial input form user

while number != 0:
    total += number # add number to total
    number = int(input("Enter a number (0 to quit): ")) # ask for another input

print("the sum of the number is:", total)
#----------------------------------------------------------------------------------------------------------------

#------------- Write a progra that find the total and average of the following list

expenses = list(map(int,input  ("Enter your expenses seprate by spaces: ").split())) # take user input and store in list 
#map function is used to convert string into integer 
total =0
index = 0 #index gives specific value store in position if index[2] in expenses value is 788
#using while loop 
while index < len(expenses):
    total += expenses[index] #add current number to total
    index +=1 
print(f"Total Expenses: {total}")
average = total / len(expenses) # calculate the average 
print(f"Average Expenses: {average}")

#---------------------   
# Brake Statement in python
# brak and continue statement help the flow of loops simple and powerfull command in python
# break is used to exit the loop immidetly and continue is used to skip the current iteration and move to the next step

#Example display the number fron 1 to 100 and ski[p 10 and 20 number

for i in range (1, 10+1):
    if i == 5:
        break # break the loop if i is equal to 5
    print(i)