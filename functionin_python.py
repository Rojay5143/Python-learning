# function is a block of code that perform a specific task 

#greet  3 people using function

def greet(name): # this is a function with tast ptint and parameter name 
    print(f"Hello {name} welcome to first example of function.") #this is a special task to perform

#calling function by passing parameter
greet("Rojay")
greet("Roshan")
greet("Rapson")

#Type of function 
# 1. No Parameter no Return type  [ It simply perform a action only]
# 2. Parameter no Return Type [ Parameter are passed to function but dosenot return any value]
#3. NO Parameter and Return Type [ No parameter are passed but function returns the value ]
#4. Parameter with Return Type

# 3 EXAMPLE OF NO PARAMETERKL;'
def greeting(): 
    print(f"Hello, I do not take any parameters")

#calling function and storing the return value
greeting_message = greeting()
#printing the return value
print(greeting_message)

#4. Parameter and return type functin example 
def add_number(a,b):
    return a+b
# substract function
def substraction(c,d):
    return c-d
#calling function add number
sum_result = add_number(5, 20)
sub_result = substraction(20, 5)
print(f"The sum of number is {sum_result}")
print(f"The diffrent of number is {sub_result}")

# use ful math functin first import math in top 
import math
# given number
number = 16 

# calculate the squreroot of number 
square_root = math.sqrt(number)
print(f"The square root of number is {square_root}")

# calculate the power of number (number^2)
power= math.pow(number,4)
print(f"{number} to the power of 4 is: {power}")

# calculate factorial (factrioal 5!)
factorial = math.factorial(5)
print(f"factorial of 5 is: {factorial}")

# given flor number is 
float_number = 16.75

# calculate the floor and celling 
floored_value = math.floor(float_number)
print(f"the floor value is; {floored_value}")

celling_value = math.ceil(float_number)
print(f"The celling value is: {celling_value}")

# challange 21
# create a function that finds a cube of a number

def cube_numbers(a):
    cube_calculation =  a*a*a
    return cube_calculation

#calling the function 
cube_of_number = cube_numbers(5)
print(f"The cube of a number 5 is: {cube_of_number}")

# create a function that finds age from birth year
current_year = 2024
def find_age ():
    birth_year = int(input(f"Enter your Birth Year in AD: ")) #changing the input to integer is imp bcz string and int callot be calculate 
    if birth_year > current_year:
        print("Birth year cannot be in future. Please enter valid year.")
        return
    age = current_year - birth_year
    print("current age is ",age)
# £culling the function 
# birth_date = find_age()
# print(f"Your Birth year is: {birth_date}")
#calling the function
find_age()
