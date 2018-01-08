import random
from fractions import Fraction
import sys

def isaprime(n):
  for i in range(2,int(n**0.5) + 1):
      if n%i == 0:
        return False
  return True

def is_probable_prime(n, k = 7):
   """use Rabin-Miller algorithm to return True (n is probably prime)
      or False (n is definitely composite)"""
   if n < 6:  # assuming n >= 0 in all cases... shortcut small cases here
      return [False, False, True, True, False, True][n]
   elif n & 1 == 0:  # should be faster than n % 2
      return False
   else:
      s, d = 0, n - 1
      while d & 1 == 0:
         s, d = s + 1, d >> 1
      # Use random.randint(2, n-2) for very large numbers
      for a in random.sample(xrange(2, min(n - 2, sys.maxint)), min(n - 4, k)):
         x = pow(a, d, n)
         if x != 1 and x + 1 != n:
            for r in xrange(1, s):
               x = pow(x, 2, n)
               if x == 1:
                  return False  # composite for sure
               elif x == n - 1:
                  a = 0  # so we know loop didn't continue to end
                  break  # could be strong liar, try another a
            if a:
               return False  # composite if we reached end of this loop
      return True  # probably prime if reached end of outer loop

def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a%b
    return a

def pollardRho(N):
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

n = 16
j = 50
numMax = 10**(n/2)

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
    if isaprime(num[i]): 
      break  
    if i == 8 and not isaprime(num[i]):
      print st,
      for l in num:
        k = pollardRho(l)
        print k,
         
      print
      count += 1
