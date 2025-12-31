def create_cart():
    cart_items = [] 

    def add_item(product, quantity=1):

        if quantity<= 0:
            print("Quantity must be positive")
            return
        
        for i, (p, q) in enumerate(cart_items):
            if p == product:
                cart_items[i] = (p, q + quantity)
                return
            
        cart_items.append((product, quantity))

    def remove_item(product, quantity=1):

        for i, (p, q) in enumerate(cart_items):
            if p == product:
                new_quantity = q - quantity

                if new_quantity <= 0:
                    cart_items.pop(i)
                else:
                    cart_items[i] = (p, new_quantity)
                return  
        return

    def get_items():
         return cart_items.copy() 
    return add_item, remove_item, get_items

if __name__ == "__main__":
    add, remove, get = create_cart()
    add((1, "Apple", 50), 3)
    add((3, "Chocolate Bar", 150), 2)
    add((1, "Apple", 50), 3)
    remove((1, "Apple", 50), 1)
    print(get())