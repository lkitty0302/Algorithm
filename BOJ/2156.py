import sys
input = sys.stdin.readline

n = int(input())

arr = [0 for _ in range(n+1)]
dp = [0 for _ in range(n+1)]

dp[0] = 0

for i in range(1, n+1):
    arr[i] = int(input())

for i in range(1, n+1):
    dp[i] = max(dp[i-2] + arr[i], dp[i-3] + arr[i-1] + arr[i])
    dp[i] = max(dp[i-1], dp[i])


print(max(dp))