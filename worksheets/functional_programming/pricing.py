# pricing.py

# TODO: Implement apply_discount(rate) returning a lambda function to apply discount to price
def apply_discount(rate):
    return lambda price:  price * (1 - rate)

# TODO: Implement apply_tax(rate) returning a lambda function to apply tax to price
def apply_tax(rate):
    return lambda price: price * (1 + rate)

# TODO: Implement calculate_total(cart_items, *pricing_funcs) applying all pricing functions in order to each product price
def calculate_total(cart_items, *pricing_func):
     total = 0
     for price, quantity in cart_items:
        for func in pricing_func:
            price = func(price)
        total += price * quantity
     return total

# Mini-Quiz: Write a one-line lambda to calculate shipping cost as flat $5 plus $1 per item
shipping = lambda items: 5 + items * 1
