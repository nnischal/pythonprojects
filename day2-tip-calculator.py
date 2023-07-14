print("Welcome to the tip calculator.!!")
bill = float(input("What was the total bil? $"))
tip = float(input("How much tip would you like to give? 10, 12, 15? "))
people = int(input("How many people to split the bill? "))
tips_as_percent = tip / 100
total_tip_amount = bill * tips_as_percent
total_bill = bill + total_tip_amount
split_bill = total_bill / people
final_amount = round(split_bill, 2)
print(f"Each person should pay ${final_amount}")