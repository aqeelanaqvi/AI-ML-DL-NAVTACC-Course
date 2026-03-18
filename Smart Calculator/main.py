import bmi
import length
import arithmetic
import temperature

choice = int(input("Select options of calculator that you want:\n 1: BMI Calculator\n 2: Arithmetic Calculator\n 3: Temperature Calculator \n 4: Length Calculator\n "))

if (choice == 1):
    print ("Now select BMI Calculator")
    height = float(input("Enter your height"))
    weight = int(input("Enter your weight"))
    BMI = bmi.calculate_bmi(weight,height)
    result =bmi.category_bmi(BMI)
    
elif(choice == 2):
    print ("Now select arithmetic calculator")
    num1= int(input("Enter number 1:"))
    num2= int(input("Enter number 2:"))
    operator = input("Select operator (+,-,*,/):")
    
    if operator == '+':
        arithmetic.add(num1, num2)
    elif operator == '-':
        arithmetic.subtract(num1, num2)
    elif operator == '*':
        arithmetic.multiply(num1, num2)
    elif operator == '/':
        if num2 == 0:
            print("Number should not be zero")
        else:
            arithmetic.divide(num1, num2)
    else:
        print("Wrong operator")
        

elif choice == 3:
    print("Now select Temperature Calculator")

    c = float(input("Enter temperature in Celsius: "))
    temperature.c_f(c)
    f = float(input("Enter temperature in Fahrenheit: "))
    temperature.f_c(f)
    
elif choice == 4:
    print("Now select Length Calculator")

    m = float(input("Enter value in meters: "))
    length.meter_to_km(m)
    length.meter_to_feet(m)

    km = float(input("Enter value in kilometers: "))
    length.km_to_meter(km)

    f = float(input("Enter value in feet: "))
    length.feet_to_meter(f)
    
        
        
        
        
      
      
    
   