# display.py

# TODO: Implement format_price(price_in_cents) function to format cents into birr string
def format_price(price_in_cents):
    birr = price_in_cents / 100
    return f"{birr:.2f} birr"

# TODO: Implement show_cart(cart_items) function that prints the cart items simply
def show_cart(cart_items):
    for (product_id, name, price), quantity in cart_items:
        print(f"{name} x {quantity}")
        

# TODO: Implement show_cart_detailed(cart_items, price_formatter_func) that uses a passed-in function for price formatting
def show_cart_detailed(cart_items, price_formatter_func):
    for (product_id, name, price), quantity in cart_items:
        formatted_price = price_formatter_func(price)
        print(f"{name} x{quantity} — {formatted_price} each")


if __name__ == "__main__":
    # Demo data
    sample_cart = [
        ((1, "Apple", 50), 3),
        ((3, "Chocolate Bar", 150), 2)
    ]
    show_cart(sample_cart)
    print()
    show_cart_detailed(sample_cart, format_price)
