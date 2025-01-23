# Voter checker
age = int (input("enter your age: "))

if age >= 18:
    print("YOU are voter.")
else:
    age_gap = 18 - age
    print(f"you are not voter. please come agter {age_gap} years")

# amount measure

item_amount = float(input("enter your amount: "))

if item_amount >= 500:
    print("The price is high")
    print("Hello")
else: 
    print(f"your amount is fare at {item_amount}")