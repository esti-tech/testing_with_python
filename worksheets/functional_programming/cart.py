def create_cart():
    """
    Create and return three functions to manage the cart:
    add_item, remove_item, get_items.

    The cart data is kept private inside this closure.
    """

    cart_items = []  # Step 1: Initialize an empty list to store (product, quantity) tuples

    def add_item(product, quantity=1):
        """
        Add a product with given quantity to the cart.
        
        Steps:
        1. Check if quantity is positive. If not, print a warning and return immediately.
        2. Loop through cart_items to check if product already exists.
        3. If found, increase its quantity.
        4. If not found, add the product with the quantity.
        5. Return nothing.
        """
        if quantity <= 0:
            print("Warning: Quantity must be positive.")
            return
        for i, (p, q) in enumerate(cart_items):
            if p == product:
                cart_items[i] = (p, q + quantity)
                return

    def remove_item(product, quantity=1):
        """
        Remove quantity of the product from the cart.
        
        Steps:
        1. Loop through cart_items to find the product.
        2. If not found, return immediately.
        3. If found, subtract the quantity.
        4. If resulting quantity is 0 or less, remove the product entirely.
        5. Return nothing.
        """
        for i, (p, q) in enumerate(cart_items):
            if p == product:
                new_quantity = q - quantity
                if new_quantity > 0:
                    cart_items[i] = (p, new_quantity)
                else:
                    cart_items.pop(i)
                return

    def get_items():
        """
        Return a copy of the current items in the cart.
        
        Steps:
        1. Create and return a shallow copy of cart_items.
        2. This protects the cart data from being modified externally.
        """
        return cart_items.copy()

    return add_item, remove_item, get_items

if __name__ == "__main__":
    add, remove, get = create_cart()
    add((1, "Apple", 50), 3)
    add((3, "Chocolate Bar", 150), 2)
    add((1, "Apple", 50), 3)
    remove((1, "Apple", 50), 1)
    print(get())