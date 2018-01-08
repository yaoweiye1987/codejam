# per m
def perm(x):
  if len(x) == 0: return [] 
  if len(x) == 1: return [x] 
  res = [] 
  for i in range(len(x)):
    for j in perm(x[:i] + x[i+1:]):
      res.append(x[i]+j)
  return res
x = 'abdc' 
print(perm(x))
