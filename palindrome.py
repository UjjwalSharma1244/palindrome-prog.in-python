
def mypow(a,b):
   return x

def get_c(n):
  s=str(n)
  return pow(10,len(s)-1)
  
def reverse(n):
	c=get_c(n)
	a=0
	while n!=0:
		a=a+(n%10)*c
		n=n//10
		c=c/10
	return a
   
def pallindrome(n):
  if n==reverse(n):
    return True

n=int(input("enter any  number"))	
print(pallindrome(n))