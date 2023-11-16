
# ------------------------------------------------------------------------------------------ #
# Title: Assignment04
# Desc: This assignment builds upon Assignment03 and allows the user to store
#       multiple students information
# Change Log: 
#   Isabella McLaughlin,11/7/2023,Created Script
# ------------------------------------------------------------------------------------------ #


#constants
MENU: str = '''
----Course Registration Program ----
Select from the following menu:
1. Register a Student for a Course
2. Show current data
3. Save data to a file
4. Exit the Program
------------------------------------
'''

FILE_NAME: str = "Enrollments.csv"

#variables
student_first_name: str = ""
student_last_name: str = ""
course_name: str = ""
student_data: dict[str,str] = {}
students: list = []  
csv_data: str = ""
file = None  
menu_choice: str  
parts:list[str]


try:
    file = open(FILE_NAME, "r")

    for row in file.readlines():
        # Transform the data from the file
        parts = row.strip().split(",")
        student_first_name = parts[0]
        student_last_name = parts[1]
        course_name = parts[2]
        student_data = {"first_name":student_first_name, "last_name":student_last_name, "course_name":course_name}
        # Load it into our collection
        students.append(student_data)

except FileNotFoundError:
    print("File not found. Creating...")
    open(FILE_NAME, "w")

except Exception as e:
    students = [] #resets the student roster in case there is an error in the file.
    print("Unknown exception",type(e), e, sep="\n") #states what the error is along with error type.

finally:
    if file and not file.closed:
    file.close()


#input / output

while (True):

    menu_choice = input(MENU)
    
    
    #menu choice 1
    if menu_choice == "1":
        try:
            student_first_name = input("Please enter your first name:  ")
            if not student_first_name.isalpha():
                raise ValueError("First name must be alphabetic")
            student_last_name = input("Please enter your last name:  ")
            if not student_last_name.isalpha():
                raise ValueError("Last name must be alphabetic")
            course_name = input("Please enter your course name: ")
            student_data = {"first_name":student_first_name, "last_name":student_last_name, "course_name":course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            print(e)

    #menu choice 2
    elif menu_choice == "2":

        print("-"*50)
        for student in students:
            print(f"Student {student["first_name"]} {student["last_name"]} is enrolled in {student["course_name"]}")
        print("-"*50)
        continue
    
    #processing
    #menu choice 3
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            for student in students:
                csv_data = f"{student["first_name"]},{student["last_name"]},{student["course_name"]}\n"
                file.write(csv_data)
            print("The following data was saved to file!")
        except Exception as e:
            print("Error saving data to file")
            print(e)
        finally:
            if file and not file.closed:
                file.close()
        for student in students:
            print(f"Student {student["first_name"]} {student["last_name"]} is enrolled in {student["course_name"]}")
        continue

    #menu choice 4
    elif menu_choice == "4":
        print("Program Ending")
        break

    #incorrect choice:
    else:
        print("Please input one of the four options")

