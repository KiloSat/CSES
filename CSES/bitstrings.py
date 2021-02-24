val = int(input())
ans=1
for i in range(val):
    ans = 2*ans
    ans = ans%(10**9+7)
print(ans)    