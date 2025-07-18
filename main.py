def info():
    pin = 2468
    account_info = {12345:0, 567890:0, 98574:0}
    return pin, account_info
    #계좌와 잔고

def check_pin(user_pin, correct_pin):
    return user_pin == correct_pin


def choose_account(user_account, correct_account):
    return user_account in correct_account

def check_balance(account_info, user_account):
    balance = account_info[user_account]
    print("Your current balance in %d is %d dollars" %(user_account, balance))

def deposit(account_info, user_account):
    added = int(input("How much do you want to deposit to account:"))
    balance = account_info[user_account] + added
    if not isinstance(balance, int):
        print("You can't deposit cents.")
    else:
        print("Deposit has been completed. Now your balance is %d" %(balance))

def withdraw(account_info, user_account):
    subs = int(input("How much do you want to withdraw from account?: "))
    balance = account_info[user_account]
    if balance <= 0 or subs > balance:
        print("You don't have enough balance.")
    else:
        balance = balance - subs
        print("Withdrawl has been completed. Now your balance is %d" %(balance))


def tasks():
    print("Please choose the task below")
    print("1. Check balance.")
    print("2. Deposit.")
    print("3. Withdraw.")


def main():
    pin, account_info = info()
    user_pin = int(input("Please Enter your pin:"))
    if check_pin(user_pin, pin):
        print("Correct pin.")
    else: 
        print("Wrong pin")
        return
        
    user_account = int(input("Please enter your account number:"))
    if choose_account(user_account, account_info):
        print("Account is in the list.")
    else: 
        print("Account is not on the list")
        return
    
    tasks()
    user_task = int(input(""))

    if user_task == 1:
        return check_balance(account_info, user_account)
    elif user_task == 2:
        return deposit(account_info, user_account)
    elif user_task == 3:
        return withdraw(account_info, user_account)
    else:
        print("Please choose the task on the list")

    

if __name__ == "__main__":
    main()