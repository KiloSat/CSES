val = int(input())
if 1<val<4:
	print('NO SOLUTION')
elif val>=4:
	arr = []
	i=2
	while i<val+1:
	    arr.append(i)
	    i+=2 
	i=1
	while i<(val+1):
	    arr.append(i)
	    i+=2
	arr = list(map(str,arr))
	print(" ".join(arr))    
else:
    print(1)
	    