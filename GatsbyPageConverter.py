class bcolors: # try to get this class from import?
    WHITE = '\033[0m' #clears all formatting.
    RED = '\033[91m'
    BLUE = '\033[94m'


#what everyone's page number is for the begining of chapter 9 used to convert pages!!
Dictionary = {"bryan":163,"kamori":163,"kai":163,"lennox":163,"hannah":163,"luciana":163,"alyssa":171,"ben":171,
              "alex":177,"esme":88,"elliot":132} #still missing some people

while True:
    while True:
        person1 = input("Person to convert from?").lower()
        try:
            Dictionary[person1]
            break
        except:
            print("That name is not on the list.")
    while True:
        try:
            input_page = int(input("Page number to convert?"))
            break
        except:
            print("That's not a valid page number!")

    previous_output = Dictionary["bryan"]
    output_list = ""
    
    print("--------------------")
    for item in Dictionary:
        if Dictionary[item] == previous_output:
            output_list = output_list + (item.capitalize()+", ")
        else:
            output_page = (input_page/Dictionary[person1]*previous_output).__floor__()
            print(f"{bcolors.RED}{output_list}{bcolors.WHITE}try page {bcolors.RED}{output_page}{bcolors.WHITE}.")
            output_list = item.capitalize()+", "
        previous_output = Dictionary[item]
    output_page = (input_page/Dictionary[person1]*previous_output).__floor__()
    print(f"{bcolors.RED}{output_list}{bcolors.WHITE}try page {bcolors.RED}{output_page}{bcolors.WHITE}.")
    print("--------------------")


#esme must add 11 to output untill I resolve this. they have 11 junk pages at begining.
        # 
        # if person1 != item:
        #     print(f"{bcolors.RED}{item.capitalize()}{bcolors.WHITE}, turn to page {bcolors.RED}{(output_page).__floor__()}{bcolors.WHITE}")
        #     #.__floor__() is a little innacurate, with stuff like 10.7 becoming 10 instead of 11.

        #print(f"{person2.capitalize()}, turn to page {output_page}")

    

    # I could do a dictionary where for page x it's a list of all the people and then once
    # it's sorted everyone it prints the "turn to page..." line for each list.


    #esme's number should be 88, but add 11 whenever you turn.