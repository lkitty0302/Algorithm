# 문제를 이해하는데 많은 시간이 걸렸던 문제
import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

def turn(n):
    idx = 2**N
    #arr 사이즈 / n
    tmp = [[0 for i in range(idx)] for i in range(idx)]
    for i in range(idx//2**n):
        for j in range(idx//2**n):
            #90도 변환
            for x in range(2**n):
                for y in range(2**n):
                    tx = i * 2**n
                    ty = j * 2**n
                    # print(tx + y, ty + 2**n - x - 1 , i * 2**n + x, j * 2**n + y)
                    tmp[tx+y][ty+ 2**n - x - 1] = arr[i * 2**n + x][j *  2**n + y]
    return tmp

def ice_check():
    tmp = deepcopy(arr)
    # print(tmp)
    for i in range(2**N):
        for j in range(2**N):
            tcnt = 0
            if tmp[i][j] <= 0:
                    continue
            
            for d in range(4):
                if i + dx[d] >= 0 and j + dy[d] >= 0 and i + dx[d] < 2**N and j + dy[d] < 2**N and tmp[i + dx[d]][j + dy[d]] > 0:
                    tcnt += 1

            if tcnt < 3:
                arr[i][j] = tmp[i][j] - 1
    # print(tmp)
    return

def bfs(x, y):
    global cnt
    if visit[x][y]:
        return

    q = deque()
    q.append((x, y))
    visit[x][y] = True

    tcnt = 1
    while q:
        xx, yy = q.popleft()
        
        for i in range(4):
            if xx + dx[i] >= 0 and yy + dy[i] >= 0 and xx + dx[i] < 2**N and yy + dy[i] < 2**N and arr[xx + dx[i]][yy + dy[i]] > 0:
                if visit[xx + dx[i]][yy + dy[i]] == True:
                    continue

                tcnt += 1
                q.append((xx + dx[i], yy + dy[i]))
                visit[xx + dx[i]][yy + dy[i]] = True
    cnt = max(cnt, tcnt)
    return 


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N, Q = map(int, input().split())

arr = [[] for i in range(2**N)]
tmp = deepcopy(arr)

for i in range(2**N):
    arr[i] = (list(map(int, input().split())))

qarr = list(map(int, input().split()))

for i in range(len(qarr)):
    #90도 회전
    arr = turn(qarr[i])
    # print(arr)
    ice_check()
    # print(arr)

visit = [[False for _ in range(2**N)] for _ in range(2**N)]

cnt = 0
ice = 0
for j in range(2**N):
    for k in range(2**N):
        if arr[j][k] > 0:
            bfs(j, k)
            ice += arr[j][k]

print(ice, cnt)
