import automobile as auto

def load_vehicles(file_name):
    
    vehicles_list = []

    auto_file = open(file_name,"r")

    next(auto_file) #skips the first line, the header.

    for line in auto_file:
        
        vehicle_data = line.split(",") #.split separates csv lines out into lists.

        vehicles_list.append(vehicle_data)
    
    return vehicles_list

def main():
    
    auto_list = []

    file_name = input("Filename: ") # filename = vehicle_data.csv

    vehicles_list = load_vehicles(file_name)
    try:
        for data in vehicles_list:
            make = data[0]
            model = data[1]
            vin = data[2]
            try:
                engine_size = float(data[3])
            except:
                engine_size = data[3]
            owner = data[4]
            year = int(data[5])

            new_auto = auto.Automobile(make,model,vin,engine_size,owner,year) #Again, self is neccecary in the class but we don't have to supply it because new_auto is the self.
            auto_list.append(new_auto)
    except:
        print(f"your file is stupid and stinky and you are a goofy goober")
    
    for vehicle in auto_list:
        print("--------------------")
        print(f"Make: {vehicle.get_make()}")
        print(f"Model: {vehicle.get_model()}")
        print(f"Vin: {vehicle.get_vin()}")
        print(f"Engine_size: {vehicle.get_engine_size()}")
        print(f"Owner: {vehicle.get_owner()}")
        print(f"Year: {vehicle.get_year()}")
        print(f"Age: {vehicle.get_age()}")
        print("--------------------")
main()


#readline() reads next line