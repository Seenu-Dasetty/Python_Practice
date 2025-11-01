print("Welcome to the tip calculator")
bill = float(input("what was the total bill? $"))
tip = int(input("how much tip would you like to give? 10, 12 or 15"))
people = int(input("how many people to split the bill?"))
total = (bill) * (tip/100) + bill
bill_per_person = total/people
print(f"each person should pay: ",{bill_per_person})