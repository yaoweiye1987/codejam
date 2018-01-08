x = [1,3,5,3,6,2,7,9] 
stack = [] 
for i in range(len(x)):
  while stack and x[i] > stack[-1]:
    print (stack.pop(), x[i]) 
  stack.append(x[i]) 

