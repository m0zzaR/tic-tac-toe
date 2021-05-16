def playPositon(pos, xy, arr):
    if pos >= 1 and pos <= 3:
        arr[0][pos - 1] = xy
    elif pos >= 4 and pos <= 6:
        arr[1][pos - 4] = xy
    elif pos >= 7 and pos <= 9:
        arr[2][pos - 7] = xy


def positionPlayed(str, pos):
    for i in str:
        if i is pos:
            return False
    return True

ticArr = [["+"] * 3 for i in range(3)]


gameState = False
winCondition = False
allNums = '1'

for i in ticArr:
        print(i)

while gameState == False and winCondition == False:
    localFlag = False

    while localFlag == False:
        print("Where would you like to play X?")
        x = int(input())
        playPositon(x, "X", ticArr)
        

        if not positionPlayed(allNums, x):
            print("Position already taken")
        else:
            localFlag = True

    allNums += str(x)
    print(allNums)

    for i in ticArr:
        print(i)

    print("Where would you like to play O?")
    y = int(input())
    playPositon(y, "O", ticArr)
    

    for i in ticArr:
        print(i)





