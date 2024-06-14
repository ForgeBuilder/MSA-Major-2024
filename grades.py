grades = []
letter_grades = []

def grade_input():
    while True:
        try:
            test_score = float(input("What is the score of the test?" ))
            
            if test_score < 0 or test_score > 100:
                print("Not a valid score!\nscores must be less than 100 and greater than 0!")
                continue
            grades.append(test_score)
            break
        except:
            print("give a valid numerical score.")
    return grade(test_score)
    

def grade(score):
    
    # print(f"Testing: {score}")

    if score >= 90:
        return("Your grade is an A!")
    elif score >= 80:
        return("Your grade is an B!")
    elif score >= 70:
        return("Your grade is an C!")
    elif score >= 60:
        return("Your grade is an D!")
    else:
        print("Stop watching ticktock or whatever how dare you!11!!1!")
        return("YOU FAILED!")
        

def main():

    while True:

        message = str(grade_input())

        letter_grades.append(message)

        print(letter_grades[len(grades)-1])

        while True:
            answer = input("Grade another test? y/n ")
            if answer == "y" or answer == "n":
                break
        if answer == "n":
            break
            
    
    print(f"\nYour Grades:\n--------------------\n")

    average = 0
    for i in range(0,len(grades)):
        print(f"Test {i+1}: {grades[i]:.2f}%   {letter_grades[i]}")

        average = average + grades[i]
    average = average/len(grades)

    print(f"\nYour average test grade was a {average:.2f} {grade(average)}")

main()


#code enter number of month, make sure its valid, tell me the season.