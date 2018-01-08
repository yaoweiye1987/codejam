import numpy as np
n = 10 
res = [0 for i in range(n+1)] 
dice = [1.,2.,3.,4.,5.,6.]
res[0] = 0 
#res[1] = sum(dice)/6. 
for i in range(1,n+1):
  temp = 0 
  for j in range(6):
    if dice[j] > res[i-1]:
      temp += dice[j]
    else:
      temp += res[i-1]
  res[i] = temp/6.
for i in range(n):
  print("%.2f" % round(res[i],2))
