a=10
b=12
c=0
if a<b and b<c:
    print("All conditions are true")
else:
    print("All conditions are not true")

if a<b or b>c:
    print("One or both the conditions are true")
else:
    print("None of the conditions are true")

  # Not operator
a=10
b=12
c=12

print(a != b)
print(b != c)

a= "Python"
b= "Codingal"

if a !=b:
    print("a, 'and', b ' are diffrent.")

    # BMI CHECKER
height= float(input("Enter your height in cm:"))
weight= float(input(" Enter your weight in kg:"))

BMI= weight/ (height/ 100)**2
 
if BMI < 18.4:
    print(" You are under weight")
elif BMI < 24.9:
    print(" You are normal")
elif BMI < 29.9:
    print(" You are over weight")
elif BMI < 34.9:
    print(" You are sevirly over weight")
elif BMI < 39.9:
    print("You are obese")
else:
    print("You are obese") 
