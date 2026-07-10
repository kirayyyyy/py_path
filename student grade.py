choice = 1
grades=[]
while 0 < choice < 5:
                choice = int(input("1. Add grade\n2. Show grades\n3. Show average\n4. Show highest grade\n5. Exit\nchoose: "))
                if choice == 1:
                    grade = int(input("Enter grade:"))
                    grades.append(grade)
                if choice == 2:
                     print ("Grades:")
                     for o in range(len(grades)):
                        print(grades[o])
                if choice == 3:
                    add = 0
                    if len(grades) == 0:
                        print("no grades yet!!")
                    else:
                        for o in range(len(grades)):
                            add += grades[o]

                        average = add / len(grades)
                        print("Average:",average)
                if choice == 4:
                    high = 0
                    for o in range (len(grades)):
                         if high <= grades[o]:
                            high = grades[o]
                    print("Highest:",high)
print("Goodbye!")