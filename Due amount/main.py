def og_amount(x):
  if x==0 or x==1:
    return 1 
  else:
    return x-og_amount

  print("The due amount is:", og_amount(7000))