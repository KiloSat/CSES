n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
val = max(arr)
s=''
j=0
while len(s)<val:
    j+=1
    s = s+(str(j))

#print(s)
#print(arr)
for i in arr:
    print(s[i-1])