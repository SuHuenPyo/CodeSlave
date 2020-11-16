'''
    이문제는 그냥 무식하게 다 계산하면서 내려갑니다. 
    생각할 부분은 없고 그냥 무식하게 계산하네요 

'''

triangle = []

n = int(input())

for i in range(0, n):
     triangle.append(list(map(int, input().split())))
    
dp = triangle
count = 2
for i in range(1, n):
    for j in range(count):
        if(j == 0):
            dp[i][j] = dp[i-1][j] + triangle[i][j]
        elif(i == j):
            dp[i][j] = dp[i-1][j-1] + triangle[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1] + triangle[i][j] , dp[i-1][j] + triangle[i][j])

    count +=1

print(max(dp[n-1]))

        
        
