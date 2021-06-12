import sys
from types import resolve_bases
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N = int(input())

arr = [['.'] * N for i in range(N)]
cnt = [[0] * N for i in range(N)]
result = [[] for i in range(N)]

str = input()

for i in range(N):
    arr[0][i] = str[i]
    result[0].append(str[i])

for i in range(N-1):
    for j in range(N):
        if arr[i][j] == '#':
            cnt[i][j] += 1
            for k in range(4):
                if 0 <= dx[k] + i < N:
                    cnt[dx[k] + i][j] += 1
                if 0 <= dy[k] + j < N:
                    cnt[i][dy[k] + j] += 1

    tmp = ''
    for j in range(N):
        if cnt[i][j] % 2 == 1:
            if arr[i][j] == '#':
                arr[i+1][j] = '.'
            else:
                arr[i+1][j] = '#'
        else:
            arr[i+1][j] = arr[i][j]
        
        result[i+1].append(arr[i+1][j])
    
for i in range(N):
    for j in range(N):
        print(result[i][j], end='')
    print()