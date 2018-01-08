nums =[ [0,0,0,0,0],\
        [0,1,1,0,0],\
        [0,1,0,0,0],\
        [0,1,1,0,1]] 
m = len(nums) 
n = len(nums[0])
def dfs(i, j, cnt):
  if i-1 > 0 and nums[i-1][j] == 1:
    nums[i-1][j] = 2
    cnt += dfs(i-1,j,1)   
  if i+1 < m and nums[i+1][j] == 1:
    nums[i+1][j] = 2
    cnt += dfs(i+1,j,1) 
  if j-1 > 0 and nums[i][j-1] == 1:
    nums[i][j-1] = 2
    cnt += dfs(i, j-1,1) 
  if j+1 < n and nums[i][j+1] == 1:
    nums[i][j+1] = 2
    cnt += dfs(i,j+1,1) 
  return cnt 
   
for i in range(m):
  for j in range(n):
    if nums[i][j] == 1:
      nums[i][j] = 2
      print (i,j,dfs(i, j, 1))
      
print (nums) 
