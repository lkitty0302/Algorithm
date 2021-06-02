# 첫번째 제출 : C++로 제출해서 컴파일 에러
# 두번째 제출 : 처음 주어진 2차원 배열에서 인구 이동이 일어나는 그룹의 갯수를 출력하는 문제로 잘못 접근해서 틀렸습니다
# 3번째 제출 : 시간초과
# 4번째 제출 : pypy3는 정답..?

#접근 방법
#BFS로 i,j (0 <= i, j < n)구간부터 열수 있는 모든 공간을 탐색한다
#열 수 있는 모든 공간을 탐색한 후 

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
                    for x, y in arrCnt:
                        arr[x][y] = sum
    if flag == True:
        cnt += 1
    else:
        break

print(cnt)
