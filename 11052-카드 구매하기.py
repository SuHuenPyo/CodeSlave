'''
    실패 실패 실패 실패 실패 실패 실패 실패 실패 실패 실패 실패 실패 실패 실패 실패 실패 실패 
'''


n = int(input())

cardPrice = [[0] for i in range(n)]

cardPrice = list(map(int, input().split()))
cardPrice = list(map(lambda x: [x], cardPrice))

for i in range(n):
    cardPrice[i].insert(0,i+1)

Average = [0] * n

##가격을 개수로 나누고
for i in range(n):
    Average[i] = cardPrice[i][1]/cardPrice[i][0]

Average = list(map(lambda x: [x], Average))
for i in range(n):
    Average[i].insert(0,i)

Average.sort(key=lambda x:x[1])
Average.reverse()

result = 0
limit = n

for i in range(0, limit):
    if( (n /cardPrice[Average[i][0]][0]) >= 1):
        result += int((n / cardPrice[Average[i][0]][0])) * cardPrice[Average[i][0]][1]
        n %= cardPrice[Average[i][0]][0]

        continue

    

if(n != 0):
    result += (n / 1) * cardPrice[0][1]
print(result)

    
    



