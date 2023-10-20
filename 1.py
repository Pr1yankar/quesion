n = int(input("Enter the No. of terms to print : "))
a , b = 0 , 1
print(a,b,sep = "\n")
for i in range(2,n):
	c = a+b
	print(c)
	a = b
	b = c

