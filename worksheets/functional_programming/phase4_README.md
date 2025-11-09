# Phase 4: Higher-Order Functions & Lambdas

## Your task

- Implement `apply_discount(rate)` and `apply_tax(rate)` to return lambda functions modifying price
- Implement `calculate_total` to apply all given pricing functions to the cart prices
- Write a one-line lambda `shipping` calculating flat $5 plus $1 per item

## Tips

- Remember lambdas can capture variables from enclosing scope
- Use `*args` to accept variable number of pricing functions
- Round final total properly and convert to int cents
