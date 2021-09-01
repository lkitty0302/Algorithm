import sys
input = sys.stdin.readline

n = int(input())

arr = []
dp = [[0 for i in range(n+1)] for i in range(n+1)]


for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n):
    for j in range(len(arr[i])):
        dp[i+1][j] = max(dp[i][j] + arr[i][j], dp[i+1][j])
        dp[i+1][j] = max(dp[i][j-1] + arr[i][j], dp[i+1][j])

print(max(dp[n]))