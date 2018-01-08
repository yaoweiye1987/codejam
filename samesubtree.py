def samesub(root):
    dic = {} 
    res = {}
  def dfs(root,dic):
    if root:
      dfs(root.left,dic)
      dfs(root.right,dic)
      if root.val in dic:
        for tmproot in dic[root.val]:
          if (root.left == None and root.right == None and tmproot.left == None and tmproot.right == None)
              or (root.left in res and tmproot.left in res[root.left] and root.right in res and tmproot.right in res[root.right]):
            if root not in res: res[root] = [tmproot] 
            else: res[root].append(tmproot) 
            if tmproot not in res: res[tmproot] = [root] 
            else: res[tmproot].append(tmproot)
        dic[root.val].append(root) 
      else: dic[root.val] = [root]  
  dfs(root, dic)
   
  
