my_set= {1,2,3}
print(my_set)

my= {1.0, "hello", (1,2,3)}
print(my)

m={1,2,3,4,2}
print(m)

my_set= set([1,2,3,2])
print(my_set,"\n")

num_set= set([0,1,2,3,4,5])
print("Original set:")
print(num_set)

num_set.pop()
print("After removing the first element from the said set:")
print(num_set,"\n")

setx={"green", "blue"}
sety={"blue","yellow"}
print("Original set elements")
print(setx)
print(sety)
print("\nIntersection of two said sets:")
setz=setx.intersection(sety)
print(setz)

setz=setx.union(sety)
print(setz)



