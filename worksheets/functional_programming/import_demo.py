# import_demo.py

# TODO: Refactor import styles:
# Use aliasing for products module
# Use direct function import for show_cart
# Import cart module normally but with an alias
# Write demo function to create a cart, add product, and display cart


import products as p
from display import show_cart
import cart as c


def demo():
    add_item, remove_item, get_items = c.create_cart()

    apple = p.get_product_by_id(1)
    chocolate = p.get_product_by_id(3)

    add_item(apple, 3)       
    add_item(chocolate, 2)   

    print("Your cart:")
    show_cart(get_items())


if __name__ == "__main__":
    demo()

