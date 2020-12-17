'''
    dp[i] = max(dp[i+T[i]] + P[i] , dp[i+1])

    역순으로 계산한다. 역순으로 계산했을떄 현재위치에 있는(i)의 소요시간만큼 dp[i의 소요시간] 값에서 현재 위치에 있는 비용을 더한값과
    전단계인 dp[i+1]을 비교한다 어차피 dp[i의 소요시간] 의 값과 더하는 부분이라 중첩되는 부분이 없다. 
    그리고 T[i] + i > n 으로 퇴사기간을 초과하게 되는 부분도 제외한다 . 

    

'''
n = int(input())

T = [0] * (n +1)
P = [0] * (n + 1)
for i in range(0, n):
    T[i], P[i] = list(map(int, input().split()))

dp = [0] * (n + 1)

for i in range(n-1, -1, -1):
    if((T[i] + i) > n ):
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+T[i]] + P[i] , dp[i+1])
    
print(dp[0])
