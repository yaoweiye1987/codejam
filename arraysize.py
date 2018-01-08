import numpy as np
n = 256 
orig = n
res = []
i = 2
while i <=n:
  if n%i == 0:
    res.append(i)
    n = n/i
    i = 2
  else:
    i += 1
print(res) 
