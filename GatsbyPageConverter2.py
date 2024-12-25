class bcolors: # try to get this class from import?
    WHITE = '\033[0m' #clears all formatting.
    RED = '\033[91m'
    BLUE = '\033[94m'

Groups = {
          "Gatsby Party":["bryan","kamori","kai","lennox","luci","wes","jay","bennie"],
          "Jazzy":["alyssa","ben"],
          "Battleship":["alex"],
          "In our prohibition era":["esme"],
          "Elliot":["elliot"],
          "West":["west"],
          "James":["james"]
        }

Group_Ch1_page = {"Gatsby Party":1,"Jazzy":1,"Battleship":3,"In our prohibition era":11,"Elliot":3,"James":7,"West":1}

Group_Ch9_page = {"Gatsby Party":163,"Jazzy":171,"Battleship":177,"In our prohibition era":99,"Elliot":132,"James":100,"West":167}

def get_person_group(person_convert_from):
    for group in Groups:
        for person in Groups[group]:
            if person == person_convert_from:
                return True, group
    return False, ""

def main():
    while True: #main loop
        while True: #input
            try:
                person_convert_from = input("Person to convert from? ").lower()
                success, group_convert_from = get_person_group(person_convert_from)
                #print(f"{str(success)} {str(group)}") #test
                if not success:
                    print(1 + "Break the code")#manual error maker
                break
            except:
                print("That person is not on the list!")
        while True:
            try:
                page = int(input("Page number?"))
                break
            except:
                print("That's not a valid page number!")

        #Convert the stuff
        page = page - (Group_Ch1_page[group_convert_from])

        for group in Groups:
            divisor = (Group_Ch9_page[group_convert_from]-Group_Ch1_page[group_convert_from])
            multiplier = (Group_Ch9_page[group]-Group_Ch1_page[group])
            result_page = (page/divisor*multiplier)+Group_Ch1_page[group]
            print(f"{bcolors.RED}{group}{bcolors.WHITE}, turn to page {bcolors.RED}{round(result_page)}{bcolors.WHITE}")
main()

# With the current system, It can't get more accurate. it nails ch1 page
# and ch9 page with no decimals, all the error is due to weird diffrences
# like how many words are on the new chapter page compare to a standard
# page, pictures, so on and soforth. 

# I could do a system where I use all the data points from the spreadsheet
# to bounce off the nearest chapter so inacuracies can't build up as much.

#Check what chapter the page is in, treat that page as page 1 for everyone
# and then multiply based on the ratio between chapter start page and next
# chapter start page. This should in theory be way more accurate because
# errors can't compound.

