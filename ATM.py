import sys
n = int(input())
arr = list(map(int, input().split()))

arr.sort()



for i in range(0, n):
    if(i == 0):
        continue
    arr[i] = arr[i - 1] + arr[i]
    

print(sum(arr))
#print(arr)