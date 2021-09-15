import sys
input = sys.stdin.readline

def move():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    shark = []

    #현재 위치와 방향
    for i in range(1, R+1):
        for j in range (1, C+1):
            if table[i][j] != 0:
                s, d, z = table[i][j]
                if d == 0 or d == 1:#위 - 움직임 횟수/R == 홀수이면 --, #아래 - 움직임 횟수/ R == 홀수이면 ++
                    xy = s % (R * 2 - 2)
                    x = i
                    y = j
                    for k in range(xy):
                        # 이 부분에서 1과 R일때 또는 1과 C일때 무조건 방향을 돌려주도록 구현해서 많이 틀렸다
                        # 예를들어 상어가 아래를 바라보고 있는데 위치가 1일 경우 방향을 돌릴 필요가 없다. 따라서 위치에 따라 방향을 고정해주어야 한다.
                        #현재 위치가 1이면 아래로 내려갈 수 있도록 x를 증가
                        if x <= 1:
                            d = 1
                        #현재 위치가 0이면 올라갈 수 있도록 x를 감소
                        elif x >= R:
                            d = 0
                        x += dx[d]
                    shark.append((x, y, s, d, z))

                elif d == 2 or d == 3:#오른쪽 - 움직임 횟수 / C == 홀수이면 ++, #왼쪽 - 움직임 횟수 / C == 홀수이면 --
                    xy = s % (C * 2 - 2)
                    x = i
                    y = j
                    for k in range(xy):
                        if y <= 1:
                            d = 2
                        elif y >= C:
                            d = 3
                        y += dy[d]
                        
                    shark.append((x, y, s, d, z))
    
    return shark

def check(shark):
    for i in range(len(shark)):
        x, y, s, d, z = shark[i]

        if table[x][y] == 0:
            table[x][y] = (s, d, z)
        else:
            if table[x][y][2] < z:
                table[x][y] = (s, d, z)
    return

R, C, M = map(int, input().split())

table = [[0 for _ in range(C+1)] for _ in range(R+1)]

for i in range(M):
    r, c, s, d, z = map(int, input().split())
    table[r][c] = (s, d-1, z)

man = 0
result = 0

#낚시꾼이 열만큼 이동했을때 멈춤
while man < C:
    #낚시꾼이 이동
    man += 1

    #현재 열(c)에서 행(r)이 가장 작은 상어 잡기
    for i in range(1, R+1):
        if table[i][man] != 0:
            s, d, z = table[i][man]
            result += z
            table[i][man] = 0
            break
    
    #상어 이동
    shark = move()
    
    for i in range(R+1):
        for j in range(C+1):
            table[i][j] = 0

    #같은칸에 두마리가 있는 경우 잡아먹음
    check(shark)

print(result)