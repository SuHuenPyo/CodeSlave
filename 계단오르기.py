import sys
n = int(input())

array = []
dp = []

for i in range(0, n):
    array.append(int(input()))



dp.append(array[0])
if(n == 1):
    print(dp[0])
    sys.exit()

dp.append(dp[0] + array[1])
if(n == 2):
    print(dp[1])
    sys.exit()


if((dp[0] + array[2]) > (array[1] + array[2])):
    dp.append(dp[0] + array[2])
else:
    dp.append(array[1] + array[2])

if(n == 3):
    print(dp[2])
    sys.exit()


for i in range(3, n):
    if((dp[i-2] + array[i]) > dp[i-3] + array[i] + array[i-1]):
        dp.append(dp[i-2] + array[i])
    else:
        dp.append(dp[i-3] + array[i] + array[i-1])

print(dp[n-1])