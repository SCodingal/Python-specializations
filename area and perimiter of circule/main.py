import math
#circumference
radius=int(input("Enter a number"))

def circumference_circle(radius):
    if radius <0:
        print("Sorry but radius can't be negtive")

circumference= 2* math.pi * radius

result= circumference_circle

print(f"The circumference of the circle with radius{radius} is: {result}")

#area
c=int(input("Enter the number"))

def calculate_circle_area(radius):

  if radius < 0:
    print("Error: Radius cannot be negative")
  
  area = math.pi * (radius ** 2)
  return area
radius=c
area = calculate_circle_area(radius)
print(f"The area of a circle with radius {radius} is: {area:.2f}")


