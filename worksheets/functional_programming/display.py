# display.py

# TODO: Implement format_price(price_in_cents) function to format cents into birr string
def format_price(price_in_cents):
    pass  # TODO

# TODO: Implement show_cart(cart_items) function that prints the cart items simply
def show_cart(cart_items):
    pass  # TODO

# TODO: Implement show_cart_detailed(cart_items, price_formatter_func) that uses a passed-in function for price formatting
def show_cart_detailed(cart_items, price_formatter_func):
    pass  # TODO
if __name__ == "__main__":
    # Demo data
    sample_cart = [
        ((1, "Apple", 50), 3),
        ((3, "Chocolate Bar", 150), 2)
    ]
    show_cart(sample_cart)
    print()
    show_cart_detailed(sample_cart, format_price)
