def my_cashier():
    print("Hello")
    print("How many items are in the cart?")

my_cashier()

def weather_condition(S1, S2):
    print('The weather is pleasant in:', S1)
    print('The weather is same in:', S2)

spring = "autumn"
autumn = "spring"

weather_condition(spring, autumn)

def add(P,Q):
    return P+Q

def subtract(P,Q):
    return P-Q

def multiply(P,Q):
    return P*Q

def divide(P,Q):
    return P/Q

print("Please select the operation.")
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")

choice = input("Please enter choice(a/b/c/d):")

num_1= int(input("Please enter the number:"))
num_2= int(input("Please enter the number:"))

if choice =='a':
    print(num_1, "+" , num_2, "=" , add(num_1,num_2))

elif choice =='b':
    print(num_1, "-" , num_2, "=" , subtract(num_1,num_2))

elif choice =='c':
    print(num_1, "*" , num_2, "=" , multiply(num_1,num_2))

elif choice =='d':
    print(num_1, "/" , num_2, "=" , divide(num_1,num_2))

else:
    print("This is an invalid input")