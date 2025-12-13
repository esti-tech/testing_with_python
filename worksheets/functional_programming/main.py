# main.py

# TODO: Implement the shopping flow inside if __name__ == "__main__"
# Steps:
# - Create a cart
# - Add a few products
# - Display the cart
# - Calculate total with a discount
# - Demonstrate clearing the cart using a utility function
# - Show cart again to confirm it's empty


def clear_cart_on_checkout(cart_items):
   
    cart_items.clear()

def display_cart(cart_items):
    
    if not cart_items:
        print("Your cart is empty.")
    else:
        print("Your cart contains:")
        for item in cart_items:
            print(f"- {item['name']} (${item['price']:.2f})")

def calculate_total(cart_items, discount=0.0):
  
    total = sum(item['price'] for item in cart_items)
    discounted_total = total * (1 - discount)
    return discounted_total

if __name__ == "__main__":
  
    cart = []

   
    cart.append({'name': 'Laptop', 'price': 999.99})
    cart.append({'name': 'Headphones', 'price': 199.99})
    cart.append({'name': 'Mouse', 'price': 49.99})

   
    display_cart(cart)

  
    discount_rate = 0.10  
    total = calculate_total(cart, discount=discount_rate)
    print(f"\nTotal after {discount_rate*100:.0f}% discount: ${total:.2f}")

    clear_cart_on_checkout(cart)

    print("\nAfter checkout:")
    display_cart(cart)
