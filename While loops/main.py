n= int(input("Enter the value of terms: "))
sum=0
i=1
while i<=n:
    sum = sum+i
    i =i+1
print("\nSum=" , sum)


w=0
while w<=0:
    print("I WILL RUN FOREVERRR")
    w=w+1

#amstrog number
num1=int(input("Enter a number: "))
summ=0
temp= num1
while temp > 0:
    digit = temp % 10
    sum+= digit ** 3
    temp//=10

if num1==summ:
    print(num1,"is a Armstrong number")
else:
    print(num1,"is not a Armstrong number")

