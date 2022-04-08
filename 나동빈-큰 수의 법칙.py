# N, M, K를 공백으로 구분하여 입력받기 
n, m, k = map(int, input().split())

#N개의 수를 공백으로 구분하여 입력받기 
data = list(map(int, input().split()))



data.sort() # 정렬

print(data)

first = data[n-1] # 가장 큰 수 
second = data[n-2] # 두 번째로 큰 수 

result = 0

while True: 
    for i in range(k): #가장 큰수 k번 더하기  #3 - 한숫자를 최대로 연속해서 더할 회수
        if(m == 0): #m이 0이라면 반복문 탈출  #5 - 최대 덧샘횟수
            break
        result += first 
        m -= 1 

    if(m == 0):
        break
    result += second #두번째로 큰 수를 한 번 더하기 
    m -= 1 # 더할 때 마다 1씩 빼기 
print(result) # 출력


