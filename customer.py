class Customer:
    def __init__(self, name):
        # Initialize _name attribute to None
        self._name = None
        # Using property setter to validate name
        self.name = name
#use property method to set the customers name 
    @property
    def name(self):
        return self._name
#use setter method to get the name attribute (strings) for the name in the customers class
    @name.setter
    def name(self, value):
        # Validate name input
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        elif len(value) < 1 or len(value) > 15:
            raise ValueError("Name must be between 1 and 15 characters.")
        # Assign validated name to _name attribute
        self._name = value

# Test samples
customer1 = Customer("NorahNjeri")
print(customer1.name)
# the  function code enables input of the customer name (it makes the code more interesting)
def create_customer():
    while True:
        try:
            name = input("Enter customer name: ")
            customer = Customer(name)
            return customer
        except ValueError as e:
            print(e)
def __str__(self):
        return self.name