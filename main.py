def info():
    pin = 2468
    account_info = {12345:0, 567890:0, 98574:0}
        #계좌와 잔고

    return pin, account_info

def check_pin(user_pin, correct_pin):
    return user_pin == correct_pin


def choose_account(user_account, correct_account):
    return user_account in correct_account

def check_balance(account_info, user_account):
    balance = account_info[user_account]
    print("Your current balance in %d is %d dollars" %(user_account, balance))

def deposit(account_info, user_account):
    try:
        added = int(input("How much do you want to deposit to account:"))
        balance = account_info[user_account] + added
        print("Deposit has been completed. Now your balance is %d" %(balance))
    except ValueError:
        print("The amount you want to deposit must be a number.")
        

def withdraw(account_info, user_account):
    try:
        subs = int(input("How much do you want to withdraw from account?: "))
        balance = account_info[user_account]
        if balance <= 0 or subs > balance:
            print("You don't have enough balance to withdraw.")
        else:
            balance = balance - subs
            print("Withdrawl has been completed. Now your balance is %d" %(balance))
    except ValueError:
        print("The amount you want to withdraw must be a number.")


def tasks():
    print("Please choose the task below")
    print("1. Check balance.")
    print("2. Deposit.")
    print("3. Withdraw.")


def main():
    pin, account_info = info()

    while True:
        try:
            user_pin = int(input("Please Enter your pin:"))
        except ValueError:
            print("Invalid pin. Try again")
            continue
        if check_pin(user_pin, pin):
            print("Correct pin.")
            break
        else: 
            print("Wrong pin")

    while True:
        try:    
            user_account = int(input("Please enter your account number:"))
        except ValueError:
            print("Invalid account. Try again")
            continue
        if choose_account(user_account, account_info):
            print("Account is in the list.")
            break
        else: 
            print("Account is not on the list")

        
    tasks()

    while True:
        try:
            user_task = int(input(""))
        except ValueError:
            print("Invalid selection. Try again")
            continue
        if user_task == 1:
            return check_balance(account_info, user_account)
        elif user_task == 2:
            print("**You can't deposit cents, only dollars are available**")
            return deposit(account_info, user_account)
        elif user_task == 3:
            print("**You can't wirhdraw cents, only dollars are available**")
            return withdraw(account_info, user_account)
        else:
            print("Please choose the task on the list")

    

if __name__ == "__main__":
    main()