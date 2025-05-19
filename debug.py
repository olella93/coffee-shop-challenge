from customer import Customer
from coffee import Coffee

# Create instances
alice = Customer("Alice")
bob = Customer("Bob")
latte = Coffee("Latte")

# Create orders
alice.create_order(latte, 5.0)  # Alice spends $5
alice.create_order(latte, 3.0)  # Alice spends $3 more (total $8)
bob.create_order(latte, 6.0)    # Bob spends $6

# Find top spender
top_spender = Customer.most_aficionado(latte)
print(f"Biggest {latte.name} fan:", top_spender.name)  # "Alice"