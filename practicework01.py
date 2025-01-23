# 1. write a prigram to print your name 
print("Rojay Chaulagain")
print('Hello i am Rojay Chaulagain') # using single '' only 

a = 7 # Declearling a constant of type int with a value of 7 
print(a)

# 2. Write a progran to find a simple interest 

# 3. Simple intrest formula I = PTR/ 100 
p = 100 
t = 2 # Time = 2 years (in years)
r = 1.5 #rate of intrest per annum 
# To calculate simple intrest (SI)
SI = int(p*t*r/100) #int function is used to print result in integer but Si always should be in float only just for knowledge
print(f"Your simple intrest is {SI}")

# # 4.  Square of number using user input
# number = int(input("Enter Your Number: "))
# square_number = number * number # calculating square of number 
# print(f"Square of the number {number} is {square_number}") #print square number 

# # 6. print full name by taking user input

# first_name = input(f"Enter Your First Name: ")
# last_name = input(f" Enter Your Last Name: ")
# print(f"Your full name is {first_name.capitalize()} {last_name.capitalize()}")


# 7. Write a progaram to find quotient and remainder of two integer

c= 9
d= 2
quotient = c/d # the result after divide
int_division = c//d # // is used to obtain result is integer only not in float not in decimal 
print (f"Integer division is: {int_division}")
print(f"the quotient is: {quotient} ")
remainder = c % d #reminder is the number that is leftover during divide in result
print(f" The reminder is: {remainder}")

#8. Write a program to swap 2 numbers 

a = 30 
b=20
print(a, b ) #this will print value of a and b
a, b = b, a
print ( a, b) # This will print value of a and b after swap value in python

# 9. Write a program to remove all white space form  string 

user_input = "hello world"
email = "John.Doe@Example.com"
sentence = "welcome to the party."
book_title = "to kill a  mockingbird             a  "
username = " alice    "
comment = "This is a bad example."
items = "apple,banana,cherry"
 # 1. str.upper()
uppercase_input = user_input.upper()
print(f"Uppercase: {uppercase_input}")
 # 2. str.lower()
normalized_email = email.lower()
print(f"Lowercase email: {normalized_email}")
 # 3. str.capitalize()
capitalized_sentence = sentence.capitalize()
print(f"Capitalized sentence: {capitalized_sentence}")
 # 4. str.title()
formatted_book_title = book_title.title()
print(f"Title Case: {formatted_book_title}")
 # 5. str.strip()
cleaned_username = username.strip()
print(f"Stripped username: '{cleaned_username}'")
 # 6. str.replace(a, b)
censored_comment = comment.replace("bad", "good")
print(f"Censored comment: {censored_comment}")
 # 7. str.split(sep)
split_items = items.split(",")
print(f"Split items: {split_items}")