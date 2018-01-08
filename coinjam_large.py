import random
from fractions import Fraction
import sys

def is_probable_prime(n, k = 7):
   if n < 6: 
      return [False, False, True, True, False, True][n]
   elif n & 1 == 0:  
      return False
   else:
      s, d = 0, n - 1
      while d & 1 == 0:
         s, d = s + 1, d >> 1
      for a in random.sample(xrange(2, min(n - 2, sys.maxint)), min(n - 4, k)):
         x = pow(a, d, n)
         if x != 1 and x + 1 != n:
            for r in xrange(1, s):
               x = pow(x, 2, n)
               if x == 1:
                  return False 
               elif x == n - 1:
                  a = 0  
                  break  
            if a:
               return False  
      return True 

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def divisor(N):
        if N%2==0:
                return 2
        x = random.randint(1, N-1)
        y = x
        c = random.randint(1, N-1)
        g = 1
        while g==1:             
                x = ((x*x)%N+c)%N
                y = ((y*y)%N+c)%N
                y = ((y*y)%N+c)%N
                g = gcd(abs(x-y),N)
        return g

n = 32
j = 500

#print primes
print 'Case #1:'
count = 0
curr = 2**(n-1)-1
while count < j: 
  curr += 2
  st = bin(curr)[2:]
  num = [0 for i in range(9)] 
  for i in range(9):
    num[i] = int(st,i+2) 
    if is_probable_prime(num[i]):   
      break  
    if i == 8 and not is_probable_prime(num[i]): 
      print st,
      for l in num:
        k = divisor(l)
        print k,
      print
      count += 1
