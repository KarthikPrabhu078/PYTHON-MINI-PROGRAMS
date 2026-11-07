#Determine whether an entered integer is even or odd using the modulus operator

num = int(input("Enter the number: "))

if num % 2 == 0:
    print("The number " , num , " is even")
else:
    print("The number ", num ," is odd")
