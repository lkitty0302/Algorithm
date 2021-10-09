import sys
from collections import deque

input = sys.stdin.readline

def dfs(node):
    if dvisit[node]:
        return
    
    danswer.append(node)
    dvisit[node] = True
    for i in range(len(g[node])):
        if dvisit[g[node][i]]:
            continue
        
        dfs(g[node][i])

    return

def bfs(node):
    visit = [False for _ in range(n+1)]
    q = deque()
    q.append(node)

    while q:
        nnode = q.popleft()
        visit[nnode] = True

        banswer.append(nnode)
        for i in range(len(g[nnode])):
            if visit[g[nnode][i]] == False:
                q.append(g[nnode][i])
                visit[g[nnode][i]] = True

    return
n, m, v = map(int, input().split())

g = [[] for _ in range(n+1)]
banswer = []
danswer = []

for i in range(m):
    a, b = map(int, input().split())

    g[a].append(b)
    g[b].append(a)

for i in range(m):
    g[i].sort()

dvisit = [False for _ in range(n+1)]
dfs(v)
bfs(v)

print(*danswer)
print(*banswer)
