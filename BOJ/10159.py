import sys
input = sys.stdin.readline

# 플로이드 와샬 알고리즘으로 문제 해결
# 하나의 정점에서 다른 모든 정점으로 가는 가능한 경로를 구해서 가능한 경우의 수를 계산한다

n = int(input())
m = int(input())

table = [[False for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, m+1):
    a, b = map(int, input().split())
    table[a][b] = True

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if table[j][i] and table[i][k]:
                table[j][k] = True

for i in range(1, n+1):
    cnt = 0
    for j in range(1, n+1):
        if i == j:
            continue
        if table[i][j] == False and table[j][i] == False:
            cnt += 1
    print(cnt)


# 1 2 3 4 5 6
#   1 2 3   5
#       5  

# 1 2 3 4 5 6
# 2 3 4   4 5 
