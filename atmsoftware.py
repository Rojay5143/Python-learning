#create a progaram that work as atm machine .. where user can 
#- check balance
#-deposit money
#-withdraw money from there account 

try:
    balance = 1000 
    print("welcome to rojay atm machine ")

    while True:
        print("1. check balance ")
        print("2. deposti money")
        print("3. withdraw money")
        print("4. exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            print(f"your current balance is : {balance: .2f}")
        elif choice == 2:
            deposit_amount = float(input((f"Enter amount to deposite: $")))
            if deposit_amount >0 :
                balance += deposit_amount
                print(f"sucessfully deposited ${deposit_amount: .2f}. Your new balance is ${balance: .2f}")
            else:
                print("deposite amount must be positive.")
        elif choice == 3:
            withdrawal_amount = float(input("Enter amount to withdraw: $"))
            if withdrawal_amount > balance:
                    print("Insufficient Fund. Please try again")
            elif withdrawal_amount <= 0:
                print("Number must be postaive")
            else:
                balance -= withdrawal_amount
                print(f"Withdral Successful $ {withdrawal_amount:.2f}. Your new balance is {balance:.2f}")
        elif choice == 4 :
            print("Thank you visite again Good luck")
            break
        else:
            print("Invalid  choice please try again")
except:
    print("Enter only numbers ")