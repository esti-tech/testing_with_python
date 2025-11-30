# Phase 1 — Student instructions

Implement add/remove and show cart behavior. Write small examples to demonstrate.

# Phase 1: Basic Functions & Data Types

## Your task

- Define the `products` list containing at least 4 products as tuples `(id, name, price_in_cents)`
- Implement `get_product_by_id(pid)` function to find a product by its id
- Implement `search_products_by_name(keyword)` to return all products whose names contain the keyword (case-insensitive)

## Tips

- Use list iteration and string methods like `.lower()` and `in`
- Test your functions by printing their results for sample inputs

## Example

```python
print(get_product_by_id(1))   # Should print product tuple for Apple
print(search_products_by_name("an"))  # Should print Banana and any other matching products