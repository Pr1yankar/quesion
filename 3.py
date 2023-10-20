try:
	n = int(input("Enter the number : "))
except:
	print("Entered value is not a integer")
	exit()
n = str(n)
print("Palindrom") if(n == n[::-1]) else print("Not an Palindrome")
