import sys
from collections import deque
from typing import Sized

def horse(x, y, cnt):
    dx = [2, 2, -2, -2, 1, -1, 1, -1]
    dy = [1, -1, 1, -1, -2, 2, 2, -2]

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < h and ny >= 0 and ny < w:
            if arr[nx][ny] == 0 and visit[nx][ny][cnt-1] > visit[x][y][cnt] + 1:
                q.append((nx, ny, cnt-1))
                visit[nx][ny][cnt-1] = visit[x][y][cnt] + 1
    return

def move(x, y, cnt):
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < h and ny >= 0 and ny < w:
            if arr[nx][ny] == 0 and visit[nx][ny][cnt] > visit[x][y][cnt] + 1:
                q.append((nx, ny, cnt))
                visit[nx][ny][cnt] = visit[x][y][cnt] + 1

    return

input = sys.stdin.readline

k = int(input())
w, h = map(int, input().split())

arr = []
visit = [[[sys.maxsize for i in range(k+1)] for j in range(w)] for z in range(h)]

for i in range(h):
    arr.append(list(map(int, input().split())))

q = deque()

q.append((0, 0, k))

visit[0][0][k] = 0

if w == 1 and h == 1 and arr[0][0] == 1:
    print(-1)
    sys.exit()

while q:
    x, y, cnt = q.popleft()
    
    if cnt > 0:
        horse(x, y, cnt)
    move(x, y, cnt)

# for i in range(k):
# result = visit[h-1][w-1][0]
result = min(visit[h-1][w-1])
print(visit)
if result == sys.maxsize:
    result = -1

print(result)