f = open('D-small-practice.in','r') 
numCases = int(f.readline()) 
def nextc(st,temp):
  st1 = ''
  n = len(temp)
  for i in st:
    if i =='0':
      st1 += temp 
    else:
      st1 += bin(2**n - 1)[2:] 
  return st1

def findindx(check, s,k):
  ''' # of items in check >= 2**k - s
    if # <= s: return their indices 
    else return []
  '''
  b = sorted(check)[::-1] 
  for i in xrange(len(b)):
    if b[i] >= 2**k - i - 1:
      break 
  if i + 1 > s: return [] 
  else:
    res = [] 
    j = 0 
    m = 2**k -i -1
    while i >=0:
      if check[j] >= m:
        res.append(j+1) 
        i -= 1
      j += 1
    return res

for case in xrange(numCases):
  st1, st2, st3 = f.readline().split()
  k = int(st1) 
  c = int(st2)
  s = int(st3)
  c1 = [bin(i)[2:].zfill(k) for i in xrange(2**(k))] 
  c2 = [bin(i)[2:].zfill(k) for i in xrange(2**(k))] 
#print c1
  while c > 1:
    for i in xrange(len(c1)):
      c2[i]  = nextc(c2[i],c1[i])
    c -= 1 
#  print c2
#print c1 
  n = len(c2[0]) 
  check = [0 for l in xrange(n)] 
  for i in xrange(len(c2)):
    for j in xrange(n):
      check[j] += int(c2[i][j]) 
 
  res = findindx(check, s,k) 

  if res == []: print 'Case #'+ str(case+1) +': IMPOSSIBLE' 
  else: 
    print 'Case #'+ str(case+1) + ':',
    for i in res:
      print i, 
    print 
