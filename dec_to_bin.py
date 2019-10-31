def recurse(ans, n):
## Your code - begin
  if (n>0):
    ans=str((n%2))+ans
    return recurse(ans,n/2)

  else:
    return ans
## Your code - end

def decToBin(n):
  return recurse("", n) 

if __name__ == "__main__":
  n = input("Enter number: ")
  output = decToBin(n)
  print output
