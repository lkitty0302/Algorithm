import sys
input = sys.stdin.readline

 #추
n = int(input())
arrn = list(map(int, input().split()))

# 구슬
m = int(input())
arrm = list(map(int, input().split()))

dp = [[0 for _ in range(15001)] for _ in range(31)]

dp[0][0] = 1
dp[0][arrn[0]] = 1

for x in range(1, n):
    for y in range(15001):
        if dp[x-1][y]:

            dp[x][y] = 1

            if 0 <= y + arrn[x] < 15001:
                dp[x][y + arrn[x]] = 1

            if 0 <= abs(y - arrn[x]) < 15001:
                dp[x][abs(y - arrn[x])] = 1

for i in arrm:
    if i > 15000:
        print("N", end = ' ')
        continue

    if dp[n-1][i] == 1:
        print("Y", end = ' ')
    else:
        print("N", end = ' ')

print("")