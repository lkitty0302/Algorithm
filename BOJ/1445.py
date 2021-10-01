import sys
import heapq

input = sys.stdin.readline

#gtable : 쓰레기가 있는 칸을 1로 표기
#ctable : 쓰레기가 인접한 칸을 1로 표기

#talbe에서 g가 인접해 있는 경우 ctable을 1로 변환, g인경우 gtable을 1로 변환
#
def bfs(x, y):
    global g_result
    global n_result
    q = []
    heapq.heappush(q, (gtable[x][y], ctable[x][y], x, y))

    while q:
        gcnt, ncnt, xx, yy = heapq.heappop(q)
        # print(gcnt, ncnt, xx, yy)

        if table[xx][yy] == 'F':
            print(visit[xx][yy][0], visit[xx][yy][1])
            return

        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m or table[nx][ny] == 'S':
                continue
            
            if visit[nx][ny][0] > gcnt + gtable[nx][ny]:
                visit[nx][ny] = (gcnt + gtable[nx][ny], ctable[nx][ny] + ncnt)
                heapq.heappush(q, (visit[nx][ny][0], ncnt + ctable[nx][ny], nx, ny))
            elif visit[nx][ny][0] == gcnt + gtable[nx][ny]:
                if visit[nx][ny][1] > ncnt + ctable[nx][ny]:
                    visit[nx][ny] = (gcnt + gtable[nx][ny], ctable[nx][ny] + ncnt)
                    heapq.heappush(q, (visit[nx][ny][0], ncnt + ctable[nx][ny], nx, ny))
                
    return


n, m = map(int, input().split())

table = [[] for _ in range(n)]
gtable = [[0 for _ in range(m)] for _ in range(n)]
ctable = [[0 for _ in range(m)] for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):
    table[i] = input()

sx = 0
sy = 0

for i in range(n):
    for j in range(m):
        cnt = 0
        if table[i][j] == 'g':
            gtable[i][j] = 1
            ctable[i][j] = 0
            continue
        

        if table[i][j] == 'S':
            sx = i
            sy = j
            continue

        if table[i][j] == 'F':
            continue

        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            
            if table[nx][ny] == 'g':
                ctable[i][j] = 1
            

visit = [[[sys.maxsize, sys.maxsize] for _ in range(m)] for _ in range(n)]
visit[sx][sy] = True
bfs(sx, sy)