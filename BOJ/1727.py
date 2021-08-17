import sys
input = sys.stdin.readline

n, m = map(int, input().split())

man = list(map(int, input().split()))
women = list(map(int, input().split()))

man.sort()
women.sort()

dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

# 현재 사람과 매칭 or 매칭
# i = 남자, j = 여자
# 

for i in range(1, n+1):
    for j in range(1, m+1):
        
        if i < j :
            dp[i][j] = min(dp[i][j-1], dp[i-1][j-1] + abs(man[i-1] - women[j-1]))
        elif i > j:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-1] + abs(man[i-1] - women[j-1]))
        else :
            dp[i][j] = dp[i-1][j-1] + abs(man[i-1] - women[j-1])
# print(dp)
# print(dp[n-1][m-1])

# 20 20 30 30 40 100
# 5 20 30 30 30 

print(dp[n][m])