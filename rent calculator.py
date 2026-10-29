rent = int(input("Enter your flat rent = "))
food = int(input("Enter the amount of food ordered = "))
electricity_spend = int(input("Enter the total elecricity spent = "))
charge_per_unit = int(input("Enter the charge per unit = "))
persons = int(input("Enter the number of persons living in flat = "))

total_bill = electricity_spend * charge_per_unit
output = (food +rent +total_bill) // persons

print("Each will pay = ", output)