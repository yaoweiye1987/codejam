n = 100000000 
numbers = set(range(n, 1, -1))
primes = [] 
while numbers:
  p = numbers.pop() 
  primes.append(p) 
  numbers.difference_update(set(range(p*2, n+1, p)))
print primes