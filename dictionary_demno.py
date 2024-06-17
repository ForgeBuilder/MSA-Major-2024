def main():
    scores = [1,4,6,7,78]
    student_names = ["Alice","Bob","Jerry","Jane","Bill"]
    for index in range(len(scores)):
        print(f"{student_names[index]}: {scores[index]}")

    #Create a dictionary of names and scores
    student_scores = {
        "Alice": 87,
        "Bob": 79,
        "Jerry": 94,
        "Sarah": 90,
    }
    
    #get bob's score
    print(student_scores["Bob"])
        


main()
