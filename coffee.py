class Coffee:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if hasattr(self, '_name'):
            raise AttributeError("Coffee name cannot be changed after creation")
        if len(value) < 3:
            raise ValueError("Name must be at least 3 characters")
        self._name = value

    def orders(self):
        from order import Order
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        return list({order.customer for order in self.orders()})

    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        prices = [order.price for order in self.orders()]
        return sum(prices) / len(prices) if prices else 0