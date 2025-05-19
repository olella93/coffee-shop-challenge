from customer import Customer
from coffee import Coffee
from order import Order

# Creating instances
customer = Customer("Alice")
coffee = Coffee("Latte")
order = Order(customer, coffee, 5.0)

# Testing relationships with readable output
print(f"{customer.name}'s orders:")
for order in customer.orders():
    print(f"- {order.coffee.name} (${order.price})")

print(f"\n{coffee.name}'s customers:")
for customer in coffee.customers():
    print(f"- {customer.name}")