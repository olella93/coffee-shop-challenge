class Order:
    def __init__(self, customer: 'Customer', coffee: 'Coffee', price: float):
        self.customer = customer
        self.coffee = coffee
        self.price = price
    
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, value: 'Customer'):
        if not isinstance(value, Customer):  # Python resolves 'Customer' at runtime
            raise TypeError("Customer must be a Customer instance")
        self._customer = value

    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, value: 'Coffee'):
        if not isinstance(value, Coffee):
            raise TypeError("Coffee must be a Coffee instance")
        self._coffee = value

