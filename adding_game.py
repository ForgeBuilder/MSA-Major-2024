import random




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
    questions = get_int_from_user("difficulty_level? (3-10) ",3,10)

    print(difficulty_level)
    print(questions)

    correct = 0

    wrong = 0

    for i in range(0,questions):
            
        num1 = (random.randint(difficulties[difficulty_level-1][0],difficulties[difficulty_level-1][1]))

        num2 = (random.randint(difficulties[difficulty_level-1][0],difficulties[difficulty_level-1][1]))

        while True:
            try:
                if int(input(f"{num1} + {num2} = ")) == num1+num2:
                    print("YAY!!!")
                    correct += 1
                else:
                    print("FUCK YOU ):< ")
                    wrong += 1
                break
            except:
                continue

    print(f"Questions wrong: {wrong}")
    print(f"Questions right: {correct}")
        
main()