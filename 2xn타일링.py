import sys


n = int(input())

if (n == 1):
    print("1")
    sys.exit()
elif (n == 2):
    print("2")
    sys.exit()

arr = [1,2]
i = 2
while(i < n):
    arr.append((arr[i-1] + arr[i-2])%10007)
    i += 1
    print(arr[i-1])
    

#print(arr[n-1])



