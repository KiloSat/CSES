num = int(input())
string = input()
arr = list(map(int,string.strip().split()))
count = 0
for i in range(1,num):
    while arr[i]<arr[i-1]:
        count += (arr[i-1]-arr[i])
        arr[i]= arr[i-1]
print(count)  