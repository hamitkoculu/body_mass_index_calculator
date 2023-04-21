#BODY MASS INDEX CALCULATOR 

# Take a values of height and weight from user

height = int(input("Your height:"))
weight = int(input("Your weight:"))

# Formula

bmi = round((weight/height ** 2) * 10000, 2)


### Body Mass Index ranges

if bmi >= 30:
    condition = "Obesity"

elif bmi >= 25:
    condition = "Owerweight"

elif bmi >= 18.5:
    condition = "Healty"

elif bmi >= 0:
    condition = "Underweight"

else:
    pass

# Output

print("Your BMI =",bmi) 
print("You are in",condition,"range." )