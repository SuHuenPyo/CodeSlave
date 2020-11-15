n, m = map(int, input().split())

arr = []

while n !=0:
    data = list(map(int, input().split()))
    data.sort()
    arr.append(data[0])
    n -= 1

arr.sort()
print(arr[len(arr)-1])
