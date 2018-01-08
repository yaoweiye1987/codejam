from multiprocessing import Pool 
import time 

def f(x):
  return x*x 

with Pool(processes=4) as pool:
  for i in range(10): 
    result = pool.apply_async(f,(i,)) 
    print (result.get(timeout=1))
  
  print(pool.map(f, range(10)))
      
  it = pool.imap(f, range(10)) 
  print(next(it))
  print(next(it))

  print(it.next(timeout=1))

  result = pool.apply_async(time.sleep,(10,))
  print(result.get(timeout=1)) 


   
