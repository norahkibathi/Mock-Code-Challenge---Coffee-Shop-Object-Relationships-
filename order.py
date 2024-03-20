from customer import Customer
from coffee import Coffee

class Order:
    def __init__(self, customer, coffee, price):
        # Initialize attributes
        self.customer = customer
        self.coffee = coffee
        self.price = price

    @property
    def price(self):
        # Getter method for price property
        print (self._price)
        return self._price
    

    @price.setter
    def price(self, value):
        #This is a  Setter method for price property  where it allows the price to be a float and betwen 1 to 10
        if not isinstance(value, float):
            raise ValueError("The price must be a float. Please enter a valid number.")
        elif not (1.0 <= value <= 10.0):
            raise ValueError("Price should be between 1.0 and 10.0.")
        self._price = value

    @property
    def coffee(self):
        # Getter method for coffee property
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        # Setter method for coffee property
        if not isinstance(value, Coffee):
            raise TypeError('Please provide an instance associated with Coffee class')
        self._coffee = value

    @property
    def customer(self):
        # Getter method for customer property
        return self._customer

    @customer.setter
    def customer(self, value):
        # Setter method for customer property
        if not isinstance(value, Customer):
            raise TypeError('Please provide an instance associated with Customer class')
        self._customer = value

    def __str__(self):
        #order details
        return f'{self.customer} wants {self.coffee} at ${self.price}'

    @classmethod
    def create_order(cls):
        #  the code enables input of the  order interactively
        customer_name = input("Enter customer name: ")
        coffee_name = input("Enter coffee name: ")
        price = float(input("Enter order price: "))
        customer = Customer(customer_name)
        coffee = Coffee(coffee_name)
       # print (cls(customer.name, coffee., price))
        return cls(customer, coffee, price)
if __name__ == "__main__":
    # Call create_order method on Order class
    final_create_order = Order.create_order()
    print("This is the order details:")
    print(final_create_order .customer.name ,final_create_order .coffee.coffee_names ,final_create_order .price )