import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dp = [[sys.maxsize for _ in range(int((2*n) ** 0.5) + 2)] for _ in range(n)]
check = [True for _ in range(n)]

for i in range(m):
    value = int(input())
    check[value-1] = False

dp[0][0] = 0
dp[1][1] = 1

for i in range(2, n):
    if check[i] == False:
        continue

    for j in range(int((2*n) ** 0.5) + 1):
        dp[i][j] = min(dp[i-j][j-1], dp[i-j][j], dp[i-j][j+1]) + 1

result = min(dp[n-1])
if result == sys.maxsize:
    print("-1")
else:
    print(result)