import sys
input = sys.stdin.readline

def dfs(n, sum):
    global result
    if n == 11:
        if result < sum:
            result = sum

        return
    
    for i in range(11):
        if player[n][i] != 0 and visit[i] == False:
            visit[i] = True
            dfs(n+1, sum + player[n][i])
            visit[i] = False
    return

T = int(input())
player = [[] for _ in range(11)]

for i in range(11):
    player[i] = list(map(int, input().split()))

visit = [False for _ in range(11)]

result = 0
for i in range(11):
    if player[0][i] != 0:
        visit[i] = True
        dfs(0, player[0][i])
        visit[i] = False

print(result)