f = open('test.txt','r') 
numCase = int(f.readline())
st1,st2 = f.readline().split() 
n = int(st1)
j = int(st2)
numMax = 10**(n/2)  
numbers = set(range(numMax,1,-1))
primes = [] 
while numbers:
  p = numbers.pop()
  primes.append(p)
  numbers.difference_update(set(range(p*2,numMax+1,p)))
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
