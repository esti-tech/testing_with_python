# products.py

# TODO: Define a list of products as tuples (id, name, price_in_cents)
products = [
    (1, "Apple", 50),
    (2, "Banana", 30),
    (3, "Chocolate Bar", 150),
    (4, "Detergent", 250),
    (5, "Eggs", 200)
]

def get_product_by_id(pid):
    for i in products:
        if i[0] == pid:
            return i
    return None

def search_products_by_name(keyword):
    for i in products:
        if keyword.lower() in i[1].lower():
            return i
    return None
def amount_search_by_price(amount):
        result = []
        for i in products:
                if i[2] == amount:
                    result.append(i)
        return result           

# Test get_product_by_id
product_result = get_product_by_id(4)
if product_result:
    print(product_result)
else:
    print("not match")

# Test search_products_by_name
search_result = search_products_by_name("detergent")
if search_result:
    print(search_result)
else:
        print("not match")
# test search result by amount
amount_result = amount_search_by_price(150)
if amount_result:
    print(amount_result)
else:
        print("not match")      
