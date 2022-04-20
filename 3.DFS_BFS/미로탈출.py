'''
동빈이는 N x M 크기의 직사각형 형태의 미로에 갇혀 있다. 미로에는 여러 마리의 괴물이 있어서 이를 피해 탈출해야한다. 
동빈이의 위치는 (1,1)이고 미로의 출구는 (N,M)의 위치에 존재하며 한번에 한 칸씩 이동 할수 있다. 
이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있다. 
미로는 반드시 탈출할 수 있는 형태로 제시된다. 이때 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오
칸을 셀 때는 시작칸과 마지막 칸을 모두 포함해서 계산한다. 

입력조건:
    첫쨰 줄에 두 정수 N,M(4<=N, M<=200)이 주어진다. 다음 N개의 줄에는 각각 M개의 정수(0 혹은 1)로 미로의 정보가 주어진다. 
    각각의 수들은 공백 없이 붙어서 입력으로 제시된다. 또한 시작 칸과 마지막 칸은 항상 1이다.

출력조건: 
    첫째 줄에 최소 이동 칸의 개수를 출력한다. 


입력예시 :
    5 6
    101010
    111111
    000001
    111111
    111111

출력예시 : 
    10
'''

from collections import deque

# N, M을 공백으로 구분하여 입력받기 
n, m = map(int, input().split())

#2차원 리스트의 맵 정보 입력받기 
graph = []
for i in range(n):
    graph.append(list(map(int,input())))


dx = [-1, 1 ,0 ,0]
dy = [0, 0, -1, 1]

def bfs(x,y):

    queue = deque()
    queue.append((x, y))

    while queue:
        
        x, y = queue.popleft()

        # 상하좌우 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 상하좌우를 바라보는데 못가는곳일때 
            if ((nx < 0) or (ny < 0) or (nx >= n) or (ny >=m)):
                continue

            #괴물이 있을 경우
            if(graph[nx][ny] == 0): 
                continue
            

            #갈 수 있는 경우 
            if(graph[nx][ny] == 1):
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    
    return graph[n-1][m-1]


print(bfs(0,0))