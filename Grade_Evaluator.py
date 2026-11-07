#Assign letter grades (A, B, C, D, F) based on numerical scores

while True:
    choice = str(input("\nDo you want to evaluate the grade of a student (y/n): "))

    if choice.upper() == "n":
        break

    name = str(input("\nEnter the name of the student: "))
    grade = int(input("Enter the total marks scored by the student (0 to 100): "))
    print("\n----------GRADE EVALUATOR----------\n")


    if grade >= 85 and grade <= 100:
        print("The grade of "+name+" is = A" )

    elif grade >= 75 and grade < 85:
        print("The grade of "+name+" is = B" )

    elif grade >= 65 and grade < 75:
        print("The grade of "+name+" is = C" )

    elif grade >= 45 and grade < 65:
        print("The grade of "+name+" is = D" )

    else:
        print("The grade of "+name+" is = F" )