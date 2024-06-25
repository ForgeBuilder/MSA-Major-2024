from student import Student
import random
import datetime

class bcolors:
    WHITE = '\033[0m' #clears all formatting.
    RED = '\033[91m'
    BLUE = '\033[94m'

def write_to_error_log(error_message):
    try:
        log_file = open("error_log.txt","a") #open 

        log_file.write(f"{datetime.now()}: {error_message}\n") #write datetime and error

        log_file.close() #close
    except Exception as err:
        print(err)

    return

#USE WITH:

# write_to_error_log("womp womp") idfk look at kristofferson example

def load_students():

    student_file = open("students.csv","r")

    next(student_file)

    student_data = []

    for line in student_file:
        
        student = line.split(",")

        student_data.append(student)
    
    return student_data


def Jane_john():
    
    Doe = [
            ["Jane","Doe","Hitting stuff with large rocks",420,4.01,100000],
            ["John","Doe","Banging head against wall",69,4.01,200000]
    ]
    return Doe[random.randint(0,1)]

def main():

    students = []

    # students.append(student.Student("Holly","Uttridge","Accounting",88,3.06,561423))
    # students.append(student.Student("Thea","Ashley","Language Arts",50,2.38,182059))

    # students[0].print_student_data()
    # students[1].print_student_data()

    student_data = load_students()

    for scholar in student_data:
        try:
            students.append(Student(scholar[0],scholar[1],scholar[2],scholar[3],scholar[4],scholar[5]))
        except:
            data = Jane_john()
            students.append(Student(data[0],data[1],data[2],data[3],data[4],data[5]))
            print(f"{bcolors.RED}Missing Values:{bcolors.WHITE} {scholar}")
    
    student_dictionary_list = []

    for scholar in students:
        student_dictionary_list.append(scholar.make_dictionary())


    while True:
        
        try:
            
            user_input = int(input("Index of student you would like to have data on: "))

            try:
                students[user_input].print_student_data()
            except:
                print("Index out of range.")
        except:
            print("Enter an integer.")
        

    



main()