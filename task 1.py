w=int(input("please enter your weight="))
h=int(input("please enter your height="))
bmi=w/(h*h)
if bmi<18.5:
    print("Underweight")
elif bmi>18.5 and bmi<25:
    print("Normal weight")
elif bmi>25 and bmi<30:
    print("Overweight")
else:
    print("Obese")

