s = '0h2abe1zy' 
ans = ''
i = 0 
while i < len(s):
  if s[i].isdigit():
    i += int(s[i]) 
    if i+1 < len(s):
      ans += s[i+1] 
      i += 2 
      print(i)
    else: break 
print(ans) 
