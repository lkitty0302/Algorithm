import sys
input = sys.stdin.readline

def dfs(x, y, sx ,sy):
    a = table[x][y]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= m or a != table[nx][ny]:
            continue
        
        if nx == sx and ny == sy:
            continue
        
        if visit[nx][ny] == True:
            return True
        
        visit[nx][ny] = True
        result = dfs(nx, ny, x, y)
        if result:
            return True
    return False

n, m = map(int, input().split())

table = [[] for _ in range(n)]

for i in range(n):
    table[i] = input()

visit = [[False for _ in range(m)] for _ in range(n)]

flag = False
for i in range(n):
    for j in range(m):
        if visit[i][j]:
            continue
        visit[i][j] = True
        result = dfs(i, j, i, j)

        if result:
            flag = True
    if flag:
        break

if flag:
    print("Yes")
else:
    print("No")