# 0으로 만들수 있는 최소한의 연산횟수를 구하시오 
import math

#방법 1 -  3으로 나누기 
#방법 2 -  2으로 나누기 
#방법 3 -  1로   빼기 


def solve():
    n = (int(input()))
    arr = [0,0,1,1,2]
    for i in range(5, n+1):
        one, two, three = math.inf, math.inf , arr[i-1]
        #three = arr[9] => 결국 2회 
        if((i%3) == 0):
            one = arr[i/3] #3으로도 됨
        if((i%2) == 0):
            two = arr[i/2] # 2로도 됨 
            #two = 결국 3회 
        
        arr.append(1 + min(one, two, three)) 
    print(arr[n])
    
solve()