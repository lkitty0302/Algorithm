import collections
import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    q = deque()
    q.append((x, y, 1))
    result = sys.maxsize

    while q:
        xx, yy, cnt = q.popleft()
        if xx == n-1 and yy == m-1:
            result = min(result, cnt)

        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]

            if nx < 0 or nx > n-1 or ny < 0 or ny > m-1:
                continue
            
            if visit[nx][ny] == False and arr[nx][ny] == '1':
                q.append((nx, ny, cnt+1))
                visit[nx][ny] = True
        
    return result

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, input().split())
arr = [0 for _ in range(n)]

visit = [[False for _ in range(m)] for _ in range(n)]

for i in range(n):
    arr[i] = list(input())
    
result = bfs(0, 0)

print(result)
