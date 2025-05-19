# Test in debug.py
from customer import Customer
from coffee import Coffee
from order import Order

# Valid cases
customer = Customer("Alice")
coffee = Coffee("Latte")
order = Order(customer, coffee, 5.0)

print(customer.name)  # "Alice"
print(coffee.name)    # "Latte"
print(order.price)    # 5.0

