import sys,getopt

def main():
  filename = '' 
  try:
    opts, args = getopt.getopt(sys.argv[1:],'i:')
  except getopt.GetoptError as err:
    print (err) 
    sys.exit()
#  print(opts)
#  print(args)
  for o, a in opts:
    if o in ('-i'):
      f = open(a,'r') 
      flag = True 
      while flag:
        try:
          x = f.readline().split()
          if x == []: flag = False 
          else: 
            for i in x:
              print(i)
        except:
          break
    else:
      sys.exit()
if __name__ == '__main__':
  main()
