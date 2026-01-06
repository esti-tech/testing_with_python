# main.py

# TODO: Implement the shopping flow inside if __name__ == "__main__"
# Steps:
# - Create a cart
# - Add a few products
# - Display the cart
# - Calculate total with a discount
# - Demonstrate clearing the cart using a utility function
# - Show cart again to confirm it's empty

from products import get_product_by_id
from cart import create_cart

def clear_cart_on_checkout(cart_items):
    cart_items.clear()

if __name__ == "__main__":
    add_item, remove_item, get_items = create_cart()

  
    apple = get_product_by_id(1)
    chocolate = get_product_by_id(3)

    add_item(apple, 3)
    add_item(chocolate, 2)

    print("Your Cart:")
    print(get_items())


    items = get_items()
    total = sum(product[2] * qty for product, qty in items)

    discount = total * 0.10
    final_total = total - discount

    print(f"\nTotal Before Discount: {total} cents")
    print(f"Discount (10%): {int(discount)} cents")
    print(f"Final Total: {int(final_total)} cents\n")

    clear_cart_on_checkout(items)

    print("Cart After Checkout (should be empty):")
    print(get_items())
