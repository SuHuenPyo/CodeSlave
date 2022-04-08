n = 1260 #만큼 잔돈 내줘야함 

count = 0 # 몇개를 거슬러 줬나 . = 결과값 

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n //coin # 몫을 구하는 연산자
    
    n%= coin
    print(n)

# 260 - 1회차 260
#
print(count)