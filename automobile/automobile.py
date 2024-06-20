#create automobile class
#Define a constructor
#The constructor is a function that executes when an object is created.

class Automobile(): #name of the class is upper case (convention)
    def __init__(self, make, model, vin, engine_size, owner, year) -> None:
        self.make = make
        self.model = model
        self.vin = vin
        self.engine_size = engine_size
        self.owner = owner
        self.year = year