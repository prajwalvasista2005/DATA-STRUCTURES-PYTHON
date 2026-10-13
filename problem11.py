def withdraw(balance,amount):
    if amount>balance:
        return "insufficient funds!"
       
    else:
        return balance-amount
result1=withdraw(1000,250)
result2=withdraw(1000,1500)
print(f"Your new balance after withdrawal is: {result1}")
print(f"Your new balance after withdrawal is: {result2}")
