while True:
    
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    n = int(input("Enter your choice: "))
    if n == 1:
        a = int(input("Enter the first element: "))
        b = int(input("Enter the second element: "))
        print("Addition = ",a+b)
        
    elif n == 2:
        a = int(input("Enter the first element: "))
        b = int(input("Enter the second element: "))
        print("Subtraction = ",a-b)
        
    elif n == 3:
        a = int(input("Enter the first element: "))
        b = int(input("Enter the second element: "))
        print("Multiplication = ",a*b)
      
    elif n == 4:
        a = int(input("Enter the first element: "))
        b = int(input("Enter the second element: "))
        if b == 0:
            print("Division by zero is not allowed.")
        else:
            print("Division = ",a/b)

    elif n == 5:
        print("Exiting the calculator. Goodbye!")
        break
    else: 
        print("Invalid choice")
       

