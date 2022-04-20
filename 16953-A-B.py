A, B = map(int, input().split())
count = 1
while True:
    if (A == B):
        break
    elif((B < A) or (B % 10 != 1 and B % 2 != 0)):
        count = -1
        break
    elif(B % 10 == 1):
        B //= 10
        count +=1
    elif(B % 2 == 0):
        B //= 2
        count += 1

print(count)
    