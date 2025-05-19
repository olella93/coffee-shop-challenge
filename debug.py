from customer import Customer
from coffee import Coffee
from order import Order

# Create instances
customer = Customer("Alice")
coffee1 = Coffee("Latte")
coffee2 = Coffee("Cappuccino")

# Create orders
order1 = Order(customer, coffee1, 4.5)
order2 = Order(customer, coffee2, 5.0)

# Test relationships
print(f"{customer.name}'s orders: {[o.coffee.name for o in customer.orders()]}")
# Output: ["Latte", "Cappuccino"]

print(f"{coffee1.name}'s customers: {[c.name for c in coffee1.customers()]}")
# Output: ["Alice"]