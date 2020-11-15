n, k = map(int, input().split())
kinds = []

for i in range(0, n):
    kinds.append(int(input()))

kinds.reverse()
result = 0

for i in range(0, len(kinds) ):
    while(k >= kinds[i]):
        result += int((k / kinds[i]))
        k %= kinds[i]

        
        if(k == 0):
            print(int(result))
            exit()

    if(k < 0):
        result -=1
        k += kinds[i]
    

    
    

