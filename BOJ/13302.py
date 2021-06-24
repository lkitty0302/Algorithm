# DFS + DP
import sys
input = sys.stdin.readline

MAX = 1000000000
N, M = map(int, input().split())

arr = list(map(int, input().split()))

dp = [[MAX for _ in range(N+1)] for _ in range(N+1)]

rd = [False for _ in range(N+1)]
for i in arr:
    rd[i] = True

def DFS(date, cp):
    #방학기간을 넘어서면 return
    if date > N:
        return 0
    #memozation
    if dp[date][cp] != MAX:
        return dp[date][cp]
    
    if rd[date] == True:
        dp[date][cp] = DFS(date + 1, cp)
        return dp[date][cp]
    
    dp[date][cp] = min(dp[date][cp], DFS(date+1, cp) + 10000)
    dp[date][cp] = min(dp[date][cp], DFS(date+3, cp+1) + 25000)
    dp[date][cp] = min(dp[date][cp], DFS(date+5, cp+2) + 37000)

    if cp >= 3:
        dp[date][cp] = min(dp[date][cp], DFS(date+1, cp-3))
    
    return dp[date][cp]

result = DFS(1, 0)

print(result)
