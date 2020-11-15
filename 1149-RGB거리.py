'''
본 문제는 현재 위치 기준에서 앞집에서 어떤색을 칠했느냐에 따라 선택할 수 있는 집이 달라지기 때문에 앞집에서 선택한 색깔마다의
최소값을 구하여 나가야 한다. 앞집에서 빨강(앞집이 빨강을 선택했을떄의 최솟값)을 선택했다면 당연 지금집에서는 빨강을 제외한 색상을 사용해야한다.
그러므로 앞집이 빨강을 선택했을떄의 최솟값, 초록을 선택했을떄의 최솟값 , 파랑을 선택했을때의 최솟값을 계산하며 나아가야한다. 

EX> dp[i][0] = 지금집[빨강] + 최솟값(dp[i-1][초록], dp[i-1][파랑])
    dp[i][0] = 지금집[초록] + 최솟값(dp[i-1][빨강], dp[i-1][파랑])
    dp[i][0] = 지금집[파랑] + 최솟값(dp[i-1][빨강], dp[i-1][초록])

이런식으로 점화식이 나온다. 항상 선택할수 있는 색깔이 3가지 이나 현재집에서 선택한 색상이 앞집에서 사용할수 없기 때문에 현재 색을 제외한색의 최솟값을
찾는방식이다.
'''



import sys 

N = int(input())

houseColor = [[0]*3 for i in range(N)]

for i in range(N):
    houseColor[i][0], houseColor[i][1], houseColor[i][2] = map(int, input().split())

dp = [[0]*3 for i in range(N)]
dp[0][0] = houseColor[0][0]
dp[0][1] = houseColor[0][1]
dp[0][2] = houseColor[0][2]

for i in range(1, N):
    dp[i][0] = houseColor[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = houseColor[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = houseColor[i][2] + min(dp[i-1][0], dp[i-1][1])

print(min(min(dp[N-1][0], dp[N-1][1]), dp[N-1][2]))

