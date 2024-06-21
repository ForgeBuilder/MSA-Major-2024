#create automobile class
#Define a constructor
#The constructor is a function that executes when an object is created.

import datetime

class Automobile(): #name of the class is upper case (convention)
    def __init__(self, make, model, vin, engine_size, owner, year) -> None:
        self.__make = make
        self.__model = model #This makes it hidden from the higherups. we make methods that allow the variables to be accessed.
        self.__vin = vin
        self.__engine_size = engine_size
        self.owner = owner
        self.__year = year

    def print_info(self):
        print(f"{self.__make} {self.__model} {self.__vin} {self.__year} {self.owner} {self.__engine_size}")
    
    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model
    
    def get_vin(self):
        return self.__vin
    
    def get_engine_size(self):
        return self.__engine_size
    
    def set_engine_size(self,new_size):
        self.__engine_size = new_size

    def get_age(self):
        time = str(datetime.datetime.now())
        current_year = int(time[0]+time[1]+time[2]+time[3])
        return current_year - self.__year
    
    def get_year(self):
        return self.__year
    
    def get_owner(self):
        return self.owner




#using mehtods like this makes it so other programs don't interfere in a way that could break the program or cause unintended functionality.

#Method is a function that is a member of a class.
