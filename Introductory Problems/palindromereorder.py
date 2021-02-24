string = input()
d = {}
if len(string)==0:
    print('NO SOLUTION')
elif len(string)==1:
    print(string)
elif len(string)%2==0:
    for i in range(len(string)):
        if string[i] in d:
            d[string[i]]+=1 
        else:    
            d[string[i]]=1
    count = 0
    numlist = list(d.values())
    for i in numlist:
        if i%2!=0:
            count+=1
    if count>1:
        print('NO SOLUTION')
    else:
        print('SOLUTION HAI BRO')
        
elif len(string)%2!=0 and len(string)>2:
    for i in range(len(string)):
        if string[i] in d:
            d[string[i]]+=1 
        else:    
            d[string[i]]=1         
    count = 0
    numlist = list(d.values())
    for i in numlist:
        if i%2!=0:
            count+=1
    if count>1:
        print('NO SOLUTION')
    else:
        print('SOLUTION HAI BRO')
        