import sys


T = int(input())

P = []

while(T != 0):
    T -= 1
    P.append(int(input()))

P.sort()
P.reverse()

result = []

result = [1,1,1]

for N in range(3, P[0]):
    result.append(result[N-2] + result[N-3])

P.reverse()

for N in range(0, len(P)):
    
    print(result[P[N]-1])

