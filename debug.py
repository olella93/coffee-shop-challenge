from customer import Customer
from coffee import Coffee

customer = Customer("Alice")
coffee = Coffee("Latte")

# Create orders
order1 = customer.create_order(coffee, 4.5)
order2 = customer.create_order(coffee, 5.0)

print(f"Total orders for {coffee.name}: {coffee.num_orders()}")  # 2
print(f"Average price: ${coffee.average_price():.2f}")          # $4.75
print(f"First order price: ${order1.price}")                   # $4.5