import string

#Function to load menu items from the file
#output is a dictionary of menu items

def get_menu_items():

    data_file = open("Menu.txt","r") # the r means we want to read.

    menu_items = {}

    for line_of_data in data_file:

        keys_and_values = line_of_data.split(",")

        item = keys_and_values[0]
        price = keys_and_values[1]
        menu_items[item] = price

    data_file.close() #It is good practice to close files.

    return menu_items



def main():

    menu_items = get_menu_items()

    menu_items = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }


    for item, value in menu_items.items():
        print(f"{item} ${value}")

    total = 0.0

    while True:

        user_input = string.capwords(input("\nWhat would you like to order?").lower())
    
        try:
            print(f"Item:\n{user_input}")
            total = total + menu_items[user_input]
            print(total)
        except:
            pass

        if user_input == "End":
            break



main()