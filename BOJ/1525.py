# bfs로 비어있는 칸에 들어갈 수 있는 숫자와 움직인 횟수를 큐에 넣어서 순차적으로 실행
# (리스트, 0x, 0y, 옮긴 횟수)

#비어있는 칸을 기준으로 상하좌우에 있는 숫자를 넣을 수 있다
#넣을 수 있는 숫자를 대입하고 큐에 넣어준다
#한번 방문했던 경우는 큐에 넣지않는데
#visit할때 list에 append()로 넣고 in으로 문자열 검색하는 방법을 사용했는데 시간초과 발생
# 생각해보니 in을 쓰더라도 list에서 in 연산이 O(N)인데 이걸 q에서 값을 뺄때마다 한다면 당연히 시간초과
#dict를 사용하면 키값으로 검색하는데 시간복잡도는 O(1) - 물론 해사충돌이 일어날 경우 O(N)이지만 여기선 해당 없음

# 틀린이유
# 없는 경우 -1을 출력해야하는데 0으로 출력해서 틀림
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