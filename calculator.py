import calculator_module

calculator=input("which calculator you want to use? "
      "\n 0=Simple calculator"
      "\n 1=Advanced calculator")
if calculator == "0":
    a = int(input("introduce first number"))
    b = int(input("introduce second number"))
    x = input("Do you want to add,deduct,multiply or divide").lower()
    if x=="add":
        print(calculator_module.add(a, b))
    elif x=="deduct":
        print(calculator_module.ded(a, b))
    elif x == "multiply":
        print(calculator_module.mul(a, b))
    elif x == "divide":
        print(calculator_module.div(a ,b))
    else:
        print("operation is not recognised, please try again")
        x = input("Do you want to add,deduct,multiply or divide").lower()
elif calculator =="1":
    height = float(input("Input your height in meters: "))
    weight = float(input("Input your weight in kilograms: "))
    print("your body mass index is: ", calculator_module.advanced_calcultor(height, weight))
