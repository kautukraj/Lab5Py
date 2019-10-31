def even_elements(l):
## Your code - begin

  return [x for x in l if x%2==0]

## Your code - end

if __name__ == "__main__":
  l = range(10)
  print "input = ", l
  print even_elements(l)
