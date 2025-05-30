# ☕ Coffee Shop Challenge

A Python implementation of a coffee shop domain model with customer ordering functionality, following strict object-oriented principles.

## Models

### `Customer`
- **Properties**:
  - `name` (string, 1-15 characters, validated)
- **Methods**:
  - `orders()`: Returns all orders by this customer
  - `coffees()`: Returns unique coffees ordered
  - `create_order(coffee, price)`: Creates new order
  - `most_aficionado(coffee)` (classmethod): Returns top spender for a coffee

### `Coffee`
- **Properties**:
  - `name` (string, ≥3 characters, immutable after creation)
- **Methods**:
  - `orders()`: Returns all orders for this coffee
  - `customers()`: Returns unique customers who ordered it
  - `num_orders()`: Returns total order count
  - `average_price()`: Calculates mean order price

### `Order` (Join Model)
- **Properties**:
  - `customer` (Customer instance)
  - `coffee` (Coffee instance)
  - `price` (float, 1.0-10.0, immutable after creation)
- **Class Variable**:
  - `all`: Tracks all order instances (single source of truth)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/coffee-shop-challenge.git
   cd coffee-shop-challenge

### `Set up the environment:`
bash
pipenv install

pipenv shell


### `Testing`

**Run the test script**:

bash

python debug.py

### `Project Structure`

coffee-shop-challenge/
├── Pipfile

├── debug.py            # Test script

├── customer.py         # Customer model

├── coffee.py           # Coffee model

├── order.py            # Order model

└── tests/              # Test directory (optional)
    ├── customer_test.py
    
    ├── coffee_test.py
    
    └── order_test.py


### `Key Features`

✔️ Strict type validation

✔️ Immutable properties where required

✔️ Circular import resolution

✔️ Single source of truth (Order.all)

✔️ Relationship navigation methods

### `Bonus`

Includes optional most_aficionado() classmethod to identify top customers by spending.

### `Author`

Richard Olella


