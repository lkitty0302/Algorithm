import sys
input = sys.stdin.readline

arr = [[] for _ in range(10)]

garo = [[False for _ in range(10)] for i in range(10)]
sero = [[False for _ in range(10)] for i in range(10)]
squere = [[False for _ in range(10)] for i in range(10)]

def dfs(x, y):
    if x == 10 and y == 1:
        for i in range(1,10):
            for j in range(9):
                print(arr[i][j], end='')
            print()
        sys.exit()
        return

    if arr[x][y-1]:
        if y == 9: dfs(x+1, 1)
        else: dfs(x, y+1)
        return

    for j in range(1,10):
        if garo[x][j] == False and sero[y][j] == False and squere[3 * ((x-1)//3) + ((y-1)//3) + 1][j] == False:
            garo[x][j] = True
            sero[y][j] = True
            squere[3 * ((x-1)//3) + ((y-1)//3) + 1][j] = True
            arr[x][y-1] = j

            if y == 9: dfs(x+1, 1)
            else: dfs(x, y+1)

            garo[x][j] = False
            sero[y][j] = False
            squere[3 * ((x-1)//3) + ((y-1)//3) + 1][j] = False
            arr[x][y-1] = 0
    
    return 0

for i in range(1,10):
    tmp = input()
    for j in range(9):
        arr[i].append(int(tmp[j]))
        garo[i][int(tmp[j])] = True
        sero[j+1][int(tmp[j])] = True
        squere[(3 * ((i-1)//3)) + (j//3) + 1][int(tmp[j])] = True

dfs(1,1)

# 000000000
# 000000000
# 000000000
# 000000000
# 000000000
# 000000000
# 000000000
# 000000000
# 000000000