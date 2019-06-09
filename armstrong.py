num=int(input("enter any number"))
sum=0
temp=num
while temp>0:
	digit =temp%10
	sum+=digit**3
	temp=temp//10
if num==sum:
	print("armstrong")
else:
	print("not armstrong")