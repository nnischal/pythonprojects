# Use of logical operators.
print("Welcome to roller coaster!!")
height = int(input("What is your actual height in cm? "))

if height >= 120:
    print("You can ride the roller coaster!!But wait a sec !!")
    age = int(input("What is your actual age?? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 60:
        bill = 0
        print("Have a free ride on us.!")
    else:
        bill = 12
        print("Adult tickets are $12.")
    
    want_photo = input("Do you want a photo of yours to be taken? Y or N. ")
    if want_photo == "Y":
        # Add $3 to the bill.
        bill += 3
    print(f"Your total bill is ${bill} ")
else:
    print("You can't ride the roller coaster!! ")