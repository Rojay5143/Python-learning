### Create a Program That Find Square of a Number using user input.
### Also use try and except

try:
    number = float(input("Enter your number: "))
    square = number*number 
    print(f"squre of number is : {square}")
except:
    print("Only accept number ")