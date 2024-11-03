'''
Drew White

M02_Lab

This code will take a user input for student's last names, aonog with their GPA and determine 
if they made the Dean's List or the Honor Roll. A student will make the Honor Roll if their 
GPA is 3.25 or above, and a student makes the Dean's List if their GPA is 3.5 or above. 
#This code will output the student's last name, along with their acceptance, then followed
their GPA.
'''

def main():
    while True:
        student_name = input("What is the students last name? ") #This takes the user input for the student's last name

        #This breaks the while loop when the user inputs "zzz" or "ZZZ", using the .upper functino to make sure
        #the uppercase and lowercase zzz closes the program
        if (student_name.upper() == "ZZZ"):
            break

        #This try...except will check if the user input for their GPA is a number, and continue to the next if invalid
        try:
            student_gpa = float(input("What is their GPA? ")) #This gets the user float user input of the student's GPA
        except:
            print("Not a valid value, please input a number for the student's GPA")
            continue
        
        #This if...elif...else determines if the student made the Honor Roll or Dean's List
        if (student_gpa >= 3.5):
            print(f"{student_name} has made the Dean's List with a GPA of: {student_gpa}")
        elif (student_gpa >= 3.25 and student_gpa < 3.5):
            print(f"{student_name} has made the Honor Roll with a GPA of: {student_gpa}")
        else: 
            print(f"{student_name} did not make the Dean's List or Honor Roll with a GPA of: {student_gpa}")
        
main()