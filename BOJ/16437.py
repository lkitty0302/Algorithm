# 
import sys
input = sys.stdin.readline

def dfs(node, visit, cnt):

    if visit[node] == True:
        return 0

    visit[node] = True
    tmp = 0

    for i in range(len(graph[node])):
        nnode = graph[node][i]
        tmp = dfs(nnode, visit, state[nnode])
        if tmp > 0:
            cnt += tmp

    return cnt

N = int(input())

visit = [False for _ in range(N+1)]

# 그래프
graph = [[] for _ in range(N + 1)]

# 양 또는 늑대 수
state = [0 for _ in range(N+1)]

for i in range(1, N):
    t, a, p = input().split()

    #늑대가 있는 경우 -로 저장
    if t == 'W':
        a = int(a) * -1
    
    state[i + 1] = int(a)

    graph[i + 1].append(int(p))
    graph[int(p)].append(i + 1)

answer = 0

for i in range(0, N+1):
    result = 0
    tmp = dfs(i, visit, state[i])
    if tmp > 0:
        answer += tmp

print(answer)