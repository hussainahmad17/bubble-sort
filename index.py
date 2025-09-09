array = [12,90,4,23,1,23,43,8,9]
for i in range(0,len(array)):
    for j in range(i+1,len(array)):
        if array[i]>array[j]:
            array[i],array[j] = array[j],array[i]

print(array)