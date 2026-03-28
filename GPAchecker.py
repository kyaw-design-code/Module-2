#####################
# GPA Checker Application for Dean's List and Honor Roll 
#
# Author: Kyaw Oo
# File name: GPAchecker.py
#
# This app will accept student names, GPAs and test if each student quailifies
# for either Dean's List or Honor Roll
#####################

# Start of program
while True:
    # Use sentinal value "ZZZ" for student's last name to quit the program.
    student_last_name = input("Please enter student's last name (Enter ZZZ to quit.): ")
    # Ask for student's last name
    if student_last_name == "ZZZ":
        break
    
    # Ask for student's first name
    student_first_name = input("Please enter student's first name: ")
    

    student_GPA = float(input("Please enter student's GPA: "))

    # Check for Dean's List
    if student_GPA >= 3.5:
        print(f"{student_first_name} {student_last_name} has made the Dean's List.")

    # Check for Honor Roll 
    elif student_GPA >= 3.25: 
        print(f"{student_first_name} {student_last_name} has made the Honor roll.")

    else:
        print(f"{student_first_name} {student_last_name} is not qualified for either the Dean's List or the Honor Roll.")
    print()

print("End of program")
    
