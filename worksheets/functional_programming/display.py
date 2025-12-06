# display.py

# TODO: Implement format_price(price_in_cents) function to format cents into birr string
def format_price(price_in_cents):
    birr = price_in_cents / 100
    return f"{birr:.2f} Birr"

# TODO: Implement show_cart(cart_items) function that prints the cart items simply
def show_cart(cart_items):
    print("Cart Summary:")
    for (product_id, name, price_in_cents), quantity in cart_items:
        print(f"- {name} x {quantity}")


# TODO: Implement show_cart_detailed(cart_items, price_formatter_func) that uses a passed-in function for price formatting
def show_cart_detailed(cart_items, price_formatter_func):
    print("Detailed Cart:")
    total_cents = 0
    for (product_id, name, price_in_cents), quantity in cart_items:
        line_total = price_in_cents * quantity
        total_cents += line_total
        print(
            f"- {name} ({price_formatter_func(price_in_cents)} each) x {quantity} "
            f"= {price_formatter_func(line_total)}"
        )
    print("-" * 40)
    print(f"Total: {price_formatter_func(total_cents)}")
if __name__ == "__main__":
    # Demo data
    sample_cart = [
        ((1, "Apple", 50), 3),
        ((3, "Chocolate Bar", 150), 2)
    ]
    show_cart(sample_cart)
    print()
    show_cart_detailed(sample_cart, format_price)
