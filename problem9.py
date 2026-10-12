def calculate_price(price,discount=10):
    discounted_price=price-(price*discount/100)
    return discounted_price

result1=calculate_price(100)
print(f"The discounted price is {result1}")
result2=calculate_price(200,20)
print(f"The discounted price is {result2}")
result3=calculate_price(500)
print(f"The discounted price is {result3}")