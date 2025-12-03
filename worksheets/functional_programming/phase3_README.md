# Phase 3: Closures

## Your task

- Implement the closure in `cart.py` with `add_item`, `remove_item`, and `get_items` functions.
- In `add_item`, do not add the product if quantity is zero or negative.
- If product already exists in the cart, update its quantity (no duplicates).
- In `remove_item`, reduce quantity or remove product if quantity reaches zero or less.

## Tips

- Remember closures capture variables from outer function.
- Use list mutation carefully to update cart_items.

## Example usage

```python
add, remove, get = create_cart()
add((1, "Apple", 50), 3)
add((3, "Chocolate Bar", 150), 2)
remove((1, "Apple", 50), 1)
print(get())  # Should show updated cart with Apple qty 2 and Chocolate Bar qty 2
