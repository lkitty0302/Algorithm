import sys
from collections import deque

input = sys.stdin.readline

def bit(x, y):
    arr = [0, 0, 0, 0]
    num = table[x][y]
    
    for i in range(4):
        tmp = bin(num & (1 << i))
        if int(tmp, 2) > 0 :
            arr[i] = 1

    return arr

def bfs(i, j ,count):
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]

    cnt = 1

    q = deque()
    q.append((i, j))

    while q:
        x, y = q.popleft()

        move = bit(x, y)

        table[x][y] = count
        for k in range(4):
            if move[k] == 0:
                nx = x + dx[k]
                ny = y + dy[k]
                
                if nx >= 0 and ny >= 0 and nx < m and ny < n and visit[nx][ny] == False:
                    cnt += 1
                    visit[nx][ny] = True
                    q.append((nx, ny))

    return cnt

def maxRoom(x, y):
    global maxRoomCnt
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]

    q = deque()
    q.append((x, y, table[x][y]))

    while q:
        xx, yy, s = q.popleft()
        
        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]

            if nx >= 0 and ny >= 0 and nx < m and ny < n and visit[nx][ny] == False:
                if s != table[nx][ny]:
                    maxRoomCnt = max(maxRoomCnt, rooms[s] + rooms[table[nx][ny]])
                
                visit[nx][ny] = True
                q.append((nx, ny, table[nx][ny]))

    return
n, m = map(int, input().split())

table = [0 for _ in range(m)]
for i in range(m):
    table[i] = list(map(int, input().split()))

visit = [[False for _ in range(n)] for _ in range(m)]
move = [0, 0, 0, 0]
rooms = []
maxRoomCnt = 0

count = 0
for i in range(m):
    for j in range(n):
        if visit[i][j] == False:
            visit[i][j] = True
            rcnt = bfs(i, j, count)
            rooms.append(rcnt)
            count += 1

visit = [[False for _ in range(n)] for _ in range(m)]

for i in range(m):
    for j in range(n):
        if visit[i][j] == False:
            maxRoom(i, j)

print(len(rooms))
print(max(rooms))        
print(maxRoomCnt)