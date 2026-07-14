students = []
def add_student():
    name = input("Name: ")
    age = int(input("Age: "))
    grade = int(input("Grade: "))
    student = {
        "name": name,
        "age": age,
        "grade": grade,
    }
    students.append(student)
    print ("Student Added")
def show_student():
    x = 1
    for student in students:
        print ("Student",x,"\n")
        print ("Name:",student["name"])
        print ("age:",student["age"])
        print ("Grade:",student["grade"],"\n")
        x += 1
def search_student():
    search = input("Student name: ")
    for student in students:
        if search == student["name"]:
            print ("Name:",student["name"])
            print ("Age:",student["age"])
            print ("Grade:",student["grade"])
            break
    else:
        print ("Student not found")
def remove_student():
    remove = input("Student name: ")
    for student in students:
        if remove == student["name"]:
            students.remove(student)
            print("Student removed")
            break
    else:
        print("Student not found")
def highest_grade():
    if len(students) > 0:
        highest = students[0]["grade"]
        hstudent = students[0]["name"]
        for student in students:
            if highest < student ["grade"]:
                highest = student["grade"]
                hstudent = student["name"]
        print ("Highest grade:",highest)
        print ("Student:",hstudent)
    else:
        print("No Students found")

def lowest_grade():
    if len(students) > 0:
        lowest = students[0]["grade"]
        lstudent = students[0]["name"]
        for student in students:
            if lowest > student ["grade"]:
                lowest = student["grade"]
                lstudent = student["name"]
        print ("Lowest grade:", lowest)
        print ("Student:",lstudent)
    else:
        print("No Students found")
def average_grade():
    num = 0
    x = 0
    if len(students) > 0:
        for student in students:
            num += student["grade"]
            x += 1
        average = num / x
        print ("The average of all grades is: ", average)
    else:
        print("No Students found")
def count_student():
    print("Total students:", len(students))
choose = 0
while choose != 9:
    choose = int(input("========== Student Analyzer ==========\n\n"
                       "1. Add Student\n"
                       "2. Show Student\n"
                       "3. Search Student\n"
                       "4. Remove Student\n"
                       "5. Highest Grade\n"
                       "6. Lowest Grade\n"
                       "7. Average Grade\n"
                       "8. Count Students\n"
                       "9. Exit\n"
                       "Choose: "))
    if choose == 1:
        add_student()
    elif choose == 2:
        show_student()
    elif choose == 3:
        search_student()
    elif choose == 4:
        remove_student()
    elif choose == 5:
        highest_grade()
    elif choose == 6:
        lowest_grade()
    elif choose == 7:
        average_grade()
    elif choose == 8:
        count_student()
print ("Have a good one !!")