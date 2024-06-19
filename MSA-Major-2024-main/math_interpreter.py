def main():
    while True:
        user_input = input("give math question!!")

        if user_input[2] == "+":
            print(float(user_input[0])+float(user_input[4]))
        elif user_input[2] == "-":
            print(float(user_input[0])-float(user_input[4]))
        elif user_input[2] == "*":
            print(float(user_input[0])*float(user_input[4]))
        elif user_input[2] == "/":
            print(float(user_input[0])/float(user_input[4]))
        else:
            print("I HATE YOU!!!!1!!!1!")
main()

#can only do one digit stuff. very bad rn.