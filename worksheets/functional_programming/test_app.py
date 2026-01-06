# test_app.py

# TODO: Write a script outside shopping_cart directory that:
# - imports shopping_cart package
# - creates a cart
# - adds two products
# - calculates total with a discount
# - displays the cart using detailed display function

from products import get_product_by_id
from cart import create_cart
from display import show_cart_detailed, format_price
from pricing import apply_discount, calculate_total


def run_test():
    # create a new cart (returns add, remove, get_items functions)
    add_item, remove_item, get_items = create_cart()

    # pick two products by id
    product1 = get_product_by_id(1)  # Apple
    product2 = get_product_by_id(3)  # Chocolate Bar

    # add products to cart
    add_item(product1, 3)
    add_item(product2, 2)

    # show cart details using the provided formatter
    cart_contents = get_items()
    print("Cart contents:")
    show_cart_detailed(cart_contents, format_price)

    # prepare (price, quantity) pairs for total calculation
    price_quantity = [(product[2], qty) for (product, qty) in cart_contents]

    # apply a 10% discount
    discount_fn = apply_discount(0.10)
    total_cents = calculate_total(price_quantity, discount_fn)

    print()
    print(f"Total after 10% discount: {format_price(total_cents)}")

    return total_cents


if __name__ == "__main__":
    run_test()

