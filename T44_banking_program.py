def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")

def deposit():
    try: 
        amount = float(input("Enter an amount to be deposited: "))
    except ValueError:
        print("not valid")
        return 0
    
    if amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        print("Done")
        return amount

def withdraw(balance):
    try:
        amount = float(input("Enter amount to be withdrawn: "))
    except ValueError:
        print("not valid")
        return 0

    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        print("Done")
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("*********************")
        print("   Banking Program   ")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("*********************")
        choice = input("Enter your choice (1-4): ")

        

        match choice:
            case '1':
                show_balance(balance)
            case '2':
                balance += deposit()
            case '3':
                balance -= withdraw(balance)
            case '4':
                is_running = False
            case _:
                print("That's not a valid choice")

    print("Thank you! Have a nice day!")

if __name__ == '__main__':
    main()

#normal: 1; 2, 1000; 3, 100; 4
#abnormal: s; 2, s; 3, k; 4
#extreme: 1; 2, 0; 3, 0; 4 