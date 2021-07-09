import sys
input = sys.stdin.readline

N, M = map(int, input().split())

table = [[0] for _ in range(M+1)]
dp = [[0 for _ in range(N+1)] for _ in range(M+1)]
path = [[0 for _ in range(N+1)] for _ in range(M+1)]

for i in range(N):
    l = list(map(int, input().split()))
    for j in range(1, len(l)):
        table[j].append(l[j])

for i in range(1, M+1):
    for j in range(1, N+1):
        for k in range(j+1):

            sum = dp[i-1][j-k] + table[i][k]

            if dp[i][j] < sum:
                dp[i][j] = sum
                path[i][j] = k

print(dp[M][N])

x = M
y = N
result = []

while x > 0:

    result.append(path[x][y])
    y -= path[x][y]
    x -= 1

result.reverse()
print(*result)




# 4 2
# 1 5 1
# 2 6 5
# 3 7 9
# 4 10 15