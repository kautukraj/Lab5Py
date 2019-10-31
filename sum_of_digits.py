def sumDigits(n):
        if (n==0):
                return 0
        else:
                d=n%10
                return (d+sumDigits(n/10))
        
## Your code - end

if __name__ == "__main__":
	n = input("Enter number: ")
	output = sumDigits(n)
	print output
