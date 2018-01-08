m = 2 
s = "3[a2[m]]2[bc]"
def findend(m,s):
  flag = 0 
  k = m
  while m < len(s):
    if s[m] == ']' and flag == 0:
      return m 
    elif s[m] == '[':
      flag += 1
      m += 1
    elif s[m] == ']' and flag != 0:
      flag -= 1
      m += 1
    else:
      m += 1
print(findend(2,s))
print(m)
