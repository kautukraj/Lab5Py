nm=''
def recurse(n, i):
## Your code - begin
    global nm
    if (i<len(n)):
        nm=str(n[i])+nm
        return recurse (n,i+1)
    else:
        if nm==str(n):
            return True
        else:
            return False
      
## Your code - end

def isPalindrome(n):
  return recurse(n, 0)


if __name__ == '__main__':
    n=raw_input("Enter string: ")
    output=isPalindrome(n)
    print output

