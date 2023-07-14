print("Welcome to roller coaster!!")
height = int(input("What is your actual height in cm? "))

if height >= 120:
    print("You can ride the roller coaster!!But wait a sec !!")
    age = int(input("What is your actual age?? "))
    if age < 12:
        print("Please pay $7.")
    if age <= 18:
        print("Please pay $10. ")
    else:
        print("Please pay $15. ")
else:
    print("You can't ride the roller coaster!! ")