count = int(input())
goal =[]
for i in range(0, count):
    goal.append(int(input()))

for i in goal:
    callZero = [0]
    callOne = [0]
    callZero.append(0)
    callOne.append(1)
    if(i == 0):
        print("1 0")
    elif(i == 1):
        print("0 1")
    else:
        for j in range(2, i+1):
            callZero.append(callOne[j-1])
            callOne.append(callZero[j-1] + callOne[j-1])
        print('{} {}'.format(callZero[i], callOne[i]))
    callZero.clear()
    callOne.clear()
        
