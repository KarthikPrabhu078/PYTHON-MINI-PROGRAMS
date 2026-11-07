#Temperature Converter: Convert values between Celsius & Fahrenheit


print("\n----------WELLCOME TO TEMPERATURE CONVERTER----------")
choice = int(input("\n 1. Celsius to Fahrenheit\n 2. Fahrenheit to celsius\n Enter you choice: "))

if choice == 1:
    celsius = float(input("\nEnter the temperature in celsius: "))
    fahrenheit = (celsius*(9/5))+32
    print("The temperature in Fahrenheit = ", fahrenheit)

elif choice == 2:
    fahrenheit = float(input("\nEnter the temperature in Fahrenheit: "))
    celsius = (fahrenheit-32)*(5/9)
    print("The temperature in Celsius = ", celsius)

else:
    print("Invalid choice")