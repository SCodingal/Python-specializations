for i in range(0,5,3):
    print(i)

for i in range(1,10,2):
    print(i)

for i in range(10,0,-1):
    print(i)

n= int(input("Enter the number whose sum you want to find:"))
sum=0
for i in range (1,n+1):
    sum= sum+i
print("\nSum =" , sum)
