from customer import Customer
from coffee import Coffee
from order import Order

# Reset Order.all for testing
Order.all = []

# Create instances
alice = Customer("Alice")
bob = Customer("Bob")
latte = Coffee("Latte")

# Create orders
order1 = alice.create_order(latte, 4.5)
order2 = alice.create_order(latte, 5.0)
order3 = bob.create_order(latte, 6.0)

# Test methods
print(f"Total orders for {latte.name}: {latte.num_orders()}")
print(f"Average price: ${latte.average_price():.2f}")        

# Test most_aficionado
top_fan = Customer.most_aficionado(latte)
print(f"Biggest {latte.name} fan:", top_fan.name) 