import sys
from collections import deque

def check(arr):
    # arr x, y에는 arr x,y-1과 반대되는 문자가 들어가야한다
    # 
    # print(arr)
    for i in range(n):
        for j in range(m):
            checkstr = ''
            cnt = 0
            if arr[i][j] == 0:
                if j == 0:
                    checkstr = arr[i-1][j][0]
                    cnt = 0
                else:
                    checkstr = arr[i][j-1][0]
                    cnt = arr[i][j-1][1]

                if checkstr == 'B':
                    if checkstr == table[i][j]:
                        arr[i][j] = (('W', cnt+1))
                    else:
                        arr[i][j] = (('W', cnt))
                else:
                    if checkstr == table[i][j]:
                        arr[i][j] = (('B', cnt+1))
                    else:
                        arr[i][j] = (('B', cnt))

    return arr
n, m = map(int, input().split())

table = [[] for _ in range(n)]
for i in range(n):
    table[i] = input()

#홀수번째 열이 B
tableB = [[0 for _ in range(m)] for _ in range(n)]

if table[0][0] == 'B':
    tableB[0][0] = (('B', 0))
else:
    tableB[0][0] = (('B', 1))

#홀수번째 열이 W
tableW = [[0 for _ in range(m)] for _ in range(n)]

if table[0][0] == 'W':
    tableW[0][0] = (('W', 0))
else:
    tableW[0][0] = (('W', 1))

tableB = check(tableB)
tableW = check(tableW)

result = sys.maxsize

for i in range(n-7):
    for j in range(m-7):
        sum1 = 0
        sum2 = 0
        for k in range(8):
            if j == 0:
                sum1 += tableB[i + k][j + 7][1] - 0
                sum2 += tableW[i + k][j + 7][1] - 0
                continue
            sum1 += tableB[i + k][j+7][1] - tableB[i + k][j-1][1]
            sum2 += tableW[i + k][j+7][1] - tableW[i + k][j-1][1]
        
        result = min(result, sum1, sum2)
    

print(result)