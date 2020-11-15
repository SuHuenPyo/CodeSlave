import sys

n = int(input())

array = [0] * n
for i in range(0, n):
    array[i] = int(input())
    
dp = [0] * 3

dp[0] = array[0]
dp[1] = array[1] + dp[0]
dp[2] = max(array[0] + array[1] , array[0] + array[2], array[1] + array[2])


if(n > 3):
    for i in range(3, n):
        dp.append(max(array[i] + dp[i-2] , array[i] + array[i-1]+ dp[i-3] , dp[i-1]))
        print(dp)


print(dp[n-1])