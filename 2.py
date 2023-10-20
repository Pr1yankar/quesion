l = [False]*101
for i in range(2,100):
	if(not l[i]):
		print(i)
		j = i
		while(j <101):
			l[j] ,j = True , j+i
del l
