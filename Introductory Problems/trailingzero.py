val = int(input())

ans,count = 0,0 
while 5**count<10**9:
    count+=1 

for i in range(1,count):
    ans += int(val/5**i) 
print(ans)  