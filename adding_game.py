import random

class bcolors:
    RED = '\033[91m'
    BLUE = '\033[94m'

    #https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal

def get_int_from_user(question,min,max):
    while True:
        try:
            output = int(input(question))
        except:
            continue
        if output > max or output < min:
            continue
        return output

def main():
    difficulties = [(0,9),(10,99),(100,999)] # these are twopuls. 

    difficulty_level = get_int_from_user("difficulty_level? (1-3) ",1,3)
    questions = get_int_from_user("number of questions? (3-10) ",3,10)

    print(difficulty_level)
    print(questions)

    correct = 0

    wrong = 0

    for i in range(0,questions):
            
        num1 = (random.randint(difficulties[difficulty_level-1][0],difficulties[difficulty_level-1][1]))

        num2 = (random.randint(difficulties[difficulty_level-1][0],difficulties[difficulty_level-1][1]))

        fails = 0
        while True:
            answer = None
            try:
                answer = int(input(f"{num1} + {num2} = "))
            except:
                pass
            if answer == num1+num2:
                print("CORRECT!!!")
                correct += 1
                break
            else:
                print("FUCK YOU!!! ):< ")
                fails += 1
                if fails == 3:
                    print(f"The answer is {num1+num2}")
                    wrong += 1
                    break

    # print(f"Questions wrong: {wrong}")
    # print(f"Questions right: {correct}")

    print(f"You got {(correct/questions*100):.2f}% correct!")


var = f"{bcolors.RED}goober"
print(var)

print(f"{bcolors.RED}yooo I got colors boi{bcolors.BLUE}")
main()





 

