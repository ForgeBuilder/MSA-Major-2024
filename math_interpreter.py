# def main():
#     while True:
#         user_input = input("give math question!!")

#         if user_input[2] == "+":
#             print(float(user_input[0])+float(user_input[4]))
#         elif user_input[2] == "-":
#             print(float(user_input[0])-float(user_input[4]))
#         elif user_input[2] == "*":
#             print(float(user_input[0])*float(user_input[4]))
#         elif user_input[2] == "/":
#             print(float(user_input[0])/float(user_input[4]))
#         else:
#             print("I HATE YOU!!!!1!!!1!")
# main()

#can only do one digit stuff. very bad rn.

def solve(user_input):
    pass



def main():
    while True:
        user_input = input("give math question!!")
        
        expression = []

        

        thing = ""

        #order of operations PEMDAS

        #convert to list

        for item in user_input:
            if item == " ":
                expression.append(thing)
                thing = ""
            else:
                thing = thing + item
        expression.append(thing)
        thing = ""

        for item in range(0,len(expression)):
            try:
                expression[item] = float(expression[item])
            except:
                pass

        print(expression)

        output = expression[0]

        for index in range(2,len(expression),2): #does not do pemdas yet but questions can get very long. also will utterly die if you input wrong.
            if expression[index-1] == "*":
                output *= expression[index]
            elif expression[index-1] == "/":
                output /= expression[index]
            elif expression[index-1] == "+":
                output += expression[index]
            elif expression[index-1] == "-":
                output -= expression[index]
        
        print(output)
                
        
        if "jeff" not in ["bob","billy","joes","GFYS"]:
            pass
            "die"

        
main()
