# bfs로 비어있는 칸에 들어갈 수 있는 숫자와 움직임 횟수를 큐에 넣어서 순차적으로 실행
# (리스트, 0x, 0y, 옮긴 횟수)

# 틀린이유
# visit을 0을 기준으로 잡아서 틀림
import sys
from collections import deque
import copy
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

arr = [0 for _ in range(3)]
d = dict()

zx = 0
zy = 0
for i in range(3):
    arr[i] = list(map(int, input().split()))
    for j in range(3):
        if arr[i][j] == 0:
            zx, zy = i, j

q = deque()
answer = [[1,2,3],[4,5,6],[7,8,0]]

v = ''
for i in range(3):
    for j in range(3):
        v += str(arr[i][j])
        
d[v] = 0
q.append((copy.deepcopy(arr), zx, zy, 0))

flag = False
result = -1
qq = 0
while q:
    tmp, x, y, cnt = q.popleft()

    if tmp == answer:
        result = cnt
        break
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        #0의 위치(x, y)에서 상,하,좌,우가 벽을 넘어가지 않으면 원래 0의 자리에 옮길 숫자를 넣어주고, 옮긴 숫자의 자리에 0 대입
        if nx >= 0 and ny >= 0 and nx < 3 and ny < 3 :
            tmp[x][y] = tmp[nx][ny]
            tmp[nx][ny] = 0

            v = ''
            for j in range(3):
                for k in range(3):
                    v += str(tmp[j][k])
            
            if v in d:
                tmp[nx][ny] = tmp[x][y]
                tmp[x][y] = 0
                continue
            else:
                d[v] = cnt+1
                q.append((copy.deepcopy(tmp), nx, ny, cnt+1))
                
                tmp[nx][ny] = tmp[x][y]
                tmp[x][y] = 0

print(result)