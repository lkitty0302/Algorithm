import sys

input = sys.stdin.readline

def dfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    visit[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= m or visit[nx][ny] == True or table[nx][ny] == 0:
            continue

        dfs(nx ,ny)
    
    return

t = int(input())

for tc in range(t):
    m, n, k = map(int, input().split())

    result = 0
    table = [[0 for _ in range(m)]for _ in range(n)]
    visit = [[False for _ in range(m)]for _ in range(n)]
    for i in range(k):
        y, x = map(int, input().split())

        table[x][y] = 1

    for i in range(n):
        for j in range(m):
            if visit[i][j] == False and table[i][j] == 1:
                dfs(i, j)
                result += 1
    
    print(result)


