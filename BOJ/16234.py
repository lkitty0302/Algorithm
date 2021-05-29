import sys
from collections import deque

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

input = sys.stdin.readline

n, l, r = map(int, input().split())

#map을 사용할 경우 iterable을 반환하기 때문에 arr[i][j]처럼 접근할 수 없음
#따라서 list로 변환해서 사용
arr = [list(map(int, input().split())) for _ in range(n)]


q = deque()

cnt = 0
while True:
    visit = [[False] * n for _ in range(n)]
    flag = False

    for i in range(n):
        for j in range(n):
            sum = 0
            arrCnt = []
            if (visit[i][j] == False):
                visit[i][j] = True
                q.append((i, j))

                while q:
                    tmpi, tmpj = q.popleft()
                    sum += arr[tmpi][tmpj]
                    arrCnt.append((tmpi, tmpj))

                    for k in range(4):
                        x = tmpi + dx[k]
                        y = tmpj + dy[k]
                        if  n > x >= 0 and n > y >= 0 and visit[x][y] == False:
                            if abs(arr[x][y] - arr[tmpi][tmpj]) >= l and abs(arr[x][y] - arr[tmpi][tmpj]) <= r:
                                q.append((x, y))
                                visit[x][y] = True

                if  len(arrCnt) > 1:
                    flag = True
                    sum //= len(arrCnt)
                    print(sum)
                    for x, y in arrCnt:
                        arr[x][y] = sum
    if flag == True:
        cnt += 1
    else:
        break
print(cnt)
