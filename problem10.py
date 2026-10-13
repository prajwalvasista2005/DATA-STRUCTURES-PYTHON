balance=500
def show_balance():
    print(f"Your current balance is: {balance}")

def spend_money(amount):
    global balance
    if amount>balance:
        print("Insufficient funds!")
    else:
        balance-=amount
        print(f"You spent {amount}, your new balance is {balance}")

show_balance()
spend_money(100)
show_balance()
