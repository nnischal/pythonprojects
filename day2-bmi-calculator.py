height = float(input("Enter your height in m: "))
weight = float(input("Enter the weight in kg: "))
bmi = round(weight/height ** 2)
print("Yoour Body Mass Index is " + str(bmi))