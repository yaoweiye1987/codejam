nums = [1,2,3,4,6] 
n = len(nums)
sumx = [sum(nums[:i]) for i in range(n+1)] 
print(sumx)

