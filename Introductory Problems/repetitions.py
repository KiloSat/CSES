sequence = input('')
count = 1 
maximum = 1

for i in range(1,len(sequence)):
    if sequence[i]==sequence[i-1]:
        count += 1
        if maximum<count:
            maximum = count
    else:
        count = 1
print(maximum)  
