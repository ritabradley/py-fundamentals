bill = float(input("What was the total bill? "))
num_of_people = int(input("How many people split the bill? "))
tip_percentage = round(float(input("What percentage of tip would you like to give? 10, 12, 15 ")) / 100, 2)


bill_total = bill / num_of_people
tip = (bill * tip_percentage) / num_of_people

total = round(bill_total + tip, 2)
print(f"Each person should pay ${total}")
