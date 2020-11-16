'''
    이친수의 경우의 개수는 i-1 의 0과 1의 개수에 의해 결정된다. 
    i-1에서 0이 2개였다면 0뒤에는 1또는 0이 올 수있다. 즉 i-1의 0의개수 곱하기 2 
    i-1에서 1이 2개였다면 0뒤에는 0만 올 수있다. 즉 i-1 의 1의개수 

'''


n = int(input())
endOne = []
endZero = []
dp = []
dp.append(1)
endOne.append(1)
endZero.append(0)

for i in range(1,n):
    dp.append((endZero[i-1]*2) + endOne[i-1])
    endZero.append(endZero[i-1] + endOne[i-1])
    endOne.append(endZero[i-1])

print(dp[n-1])



    
    
