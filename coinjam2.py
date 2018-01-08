import numpy as np
def primesfrom2to(n):
  sieve = np.ones(n/3 + (n%6==2), dtype = np.bool)
  sieve[0] = False
  for i in xrange(int(n**0.5)/3+1):
     if sieve[i]:
        k = 3*i + 1|1
        sieve[((k*k)/3)::2*k] = False
        sieve[(k*k+4*k-2*k*(i&1))/3::2*k] = False
  return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]
f = open('test.txt','r') 
numCase = int(f.readline())
st1,st2 = f.readline().split() 
n = int(st1)
j = int(st2)
numMax = 10**16  
primes = primesfrom2to(numMax)
#print primes
print 'Case #1:'
count = 0
curr = 2**(n-1)-1
while count < j and curr < numMax:
  curr += 2
  st = bin(curr)[2:]
  num = [0 for i in range(9)] 
  for i in range(9):
    num[i] = int(st,i+2) 
    if num[i] in primes: 
      break  
    if i == 8 and num[i] not in primes:
      print st,
      for l in num:
        for k in primes:  
          if l%k == 0: 
            print k,
            break 
      print
      count += 1
