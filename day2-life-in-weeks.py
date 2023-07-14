age = input("What is your current age? ")

age_as_int = int(age)
years_remaining = 90 - age_as_int
months_remaining = years_remaining * 12
weeks_remaining = years_remaining * 52
days_remaing = years_remaining * 365

print(f"You have {days_remaing} days, {weeks_remaining} weeks and {months_remaining} months left.")