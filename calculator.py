while(1):
    
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
        
    if n == 2:
        a = int(input("Enter the first element: "))
        b = int(input("Enter the second element: "))
        print("Subtraction = ",a-b)
        
    if n == 3:
        a = int(input("Enter the first element: "))
        b = int(input("Enter the second element: "))
        print("Multiplication = ",a*b)
      
    if n == 4:
        a = int(input("Enter the first element: "))
        b = int(input("Enter the second element: "))
        print("Division = ",a/b)

    if n == 5:
        exit(0) 

