def main():
    #Capitalise a string
    name = "elliot"
    last_name = "KOPITSKE"

    print(name.capitalize())
    print(name.upper())
    print(name.encode())
    print(last_name.lower().capitalize())


    for letter in name:
        print(letter)
    
    name_dot_longness = len(name)

    print(f"name_dot_longness {name_dot_longness}\n")

    sentance = "I have a cat. My cat is cute. Do you want a cat?"
    cat_count = 0
    state = None 

    for letter in sentance:
        if letter == "c" and state == None:
            state = "c"
        if letter == "a" and state == "c":
            state = "a"
        if letter == "t" and state == "a":
            state = None
            cat_count += 1
        if letter != "c" and letter != "a" and letter != "t":
            state = None


    print(f"This sentance has the word cat {cat_count} times.")

    


#oops I did it ^^^







main()

