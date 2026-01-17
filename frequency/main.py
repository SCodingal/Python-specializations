test_dict={"codingal":2,"Code":2,"for":2,"Coding":1,"is": 3}
print("The original dictionary:"+str(test_dict))

K=2
res=0
for key in test_dict:
    if test_dict[key]==K:
        res=res+1

print("Frequency of K is:"+str(res))