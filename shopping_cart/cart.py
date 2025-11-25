# Shopping Cart Module

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_total(self):
        return sum(item.price for item in self.items) # Assume each item has a price attribute

    def clear_cart(self):
        self.items = []

# Example usage:
if __name__ == '__main__':
    cart = ShoppingCart()
    # Add items to the cart
    # cart.add_item(item)
