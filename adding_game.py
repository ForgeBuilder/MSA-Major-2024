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

    print(random.randint(difficulties[difficulty_level-1][0],difficulties[difficulty_level-1][1]))

       
main()