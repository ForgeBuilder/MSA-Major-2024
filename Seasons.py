def get_season():
    while True:
        try:
            answer = int(input("What mounth is it? Please supply a number: "))
            if answer <= 12:
                break
            else:
                print("A month less than 12 dingus ._.")
        except:
            pass
    if answer == 12:
        return("winter")
    elif answer >= 9:
        return("fall")
    elif answer >= 6:
        return("summer")
    elif answer >= 3:
        return("spring")
    else:
        return("winter")


def main():
    print(get_season())

main()