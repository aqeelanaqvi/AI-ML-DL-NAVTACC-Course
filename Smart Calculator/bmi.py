def calculate_bmi(weight,height):
    feet = height *0.03048
    BMI = weight / (feet ** 2)
    print("Your BMI value is :", BMI)
    return BMI
def category_bmi(BMI):
    if BMI < 18.5:
        print("You are underweight")
    elif BMI <= 24.9:
        print("You are normal")
    elif BMI <= 29.9:
        print("You are overweight")
    else:
        print("You are obese")
    