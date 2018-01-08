from multiprocessing import Pool 
import time 

now = time.time

def foo(n):
  for i in range(n):
    yield i 

def bar(i):
  print(now(),i) 
  time.sleep(1)
  print(now(),i) 

for key in foo(3):
  print(key)

pool = Pool(2) 

pool.map(bar,foo(6)) 

pool.close()
pool.join()
