print("Half Pyramid Pattern of Stars (*): ")
n= int(input("Enter the number of rows"))
#outer loop
for i in range(n):
  #inner loop
  for j in range (i+1):
    print("*", end="")
  print()

print("Half Pyramid Pattern of Stars (*): ")
n= int(input("Enter the number of rows"))
for i in range(n,0,-1):
  for j in range (i):
    print("*", end="")
  print()

print("Half Pyramid Pattern of Numbers : ")
n= int(input("Enter the number of rows"))
for i in range(n):
  for j in range (i+1):
    print(i+1, end=" ")
  print()