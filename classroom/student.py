
class Student():
    def __init__(self,first_name,last_name,major,credit_hours,gpa,id_number):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__major = major
        self.__credit_hours = credit_hours
        self.__gpa = gpa
        self.__id_number = id_number

    def get_class_level(self):
        if self.__credit_hours <= 30:
            return "Freshman"
        elif self.__credit_hours <= 60:
            return "Sophmore"
        elif self.__credit_hours <= 90:
            return "Junior"
        else:
            return "Senior"
        
    def print_student_data(self):
        print(f"-------------------------------\nFirst Name: {self.__first_name}\nLast Name: {self.__last_name}\nMajor: {self.__major}\nCredit Hours: {self.__credit_hours}\nGPA: {self.__gpa}\nID Number: {self.__id_number}")

    def update_credit_hours(self,hours):
        self.__credit_hours += hours