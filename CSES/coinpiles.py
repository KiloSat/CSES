val = int(input())
ans = []
for i in range(val):
    num = input('')
    arr = list(map(int,num.strip().split()))
    if sum(arr)%3==0 and (max(arr)<=2*min(arr)) or (arr[0]==arr[1]==0):
        ans.append('YES')
    else:
        ans.append('NO')

for i in ans:
    print(i)