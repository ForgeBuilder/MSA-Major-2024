import automobile 

def main():

    auto1 = automobile.Automobile("Ford","Focus", "1234",2.2,"Alex",2013)
    auto2 = automobile.Automobile("Honda","Accord","23456",3.0,"Bob",2017)

    auto1.print_info() #self is passed by the first auto1 here. even tho func calls for self, this satisfies it bc we are using auto1. and not automobile. it allready has self.
    auto2.print_info()

    auto2.__year = 2020 #This fails because you can't edit an __!

    auto1.owner = "Cyd"

    auto1.print_info()
    auto2.print_info()

    print(auto1.get_age())

    #Basic principles of object programing.

    #polymorphisum
        #An object can take many forms
    #inheritance
        #One class can inherit from another class
    #incapsulation
        #Securing the data that belongs to your class, data security.


    automobile_list = []
    automobile_list.append(auto1)
    automobile_list.append(auto2)

    print(f"\nGetting automobiles from a list\n-----------------------------------------")

    for auto in automobile_list:
        auto.print_info()

main()