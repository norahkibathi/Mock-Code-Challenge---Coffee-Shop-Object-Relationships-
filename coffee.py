class Coffee:
    ## the code intializes the coffe-name and count  of coffee types . 
     _coffee_names = []
     instance_count = 0  
    
     def __init__(self, coffee_type):
        # ensures that the instances creates are not more than 3 and the coffe-types are in string
        if Coffee.instance_count >= 3:
            raise ValueError("Cannot create more than three instances of Coffee.")
        
        # ensures validation of  the coffee type
        if not isinstance(coffee_type, str):
            raise ValueError("Name must be a string.")
        elif len(coffee_type) < 3:
            raise ValueError("Name must be at least 3 characters long.")
        
        # enables adding of the coffe names 
        self._coffee_names.append(coffee_type)
        
        
        Coffee.instance_count  += 1
     #The following functions allow for adding new attributes to each individual coffee object.
            
        @classmethod
        def coffee_names(cls):
            return cls._coffee_names.copy()   