# 다익스트라로 최소 거리를 찾아 cost를 업데이트하고, cost를 업그레이드 할 때 경로도 같이 저장
import sys
import heapq
input = sys.stdin.readline

def dijk(start):
    
    visit = [False for _ in range(N+1)]
    q = []
    
    for i in range(len(arr[start])):
        d[arr[start][i][0]] = (arr[start][i][1], start)
        heapq.heappush(q, (arr[start][i][1], arr[start][i][0]))
    visit[start] = True
    d[start] = (0, 0)

    while q:
        cost, end = heapq.heappop(q)
        visit[end] = True

        for i in range(len(arr[end])):
            node = arr[end][i][0]
            ncost = arr[end][i][1]
            
            if visit[node] == False:
                if d[node][0] > d[end][0] + ncost:
                    d[node] = (d[end][0] + ncost, end)
                    heapq.heappush(q, (cost + arr[end][i][1], arr[end][i][0]))
        
    return
N, M = map(int, input().split())

arr = [[] for i in range(N+1)]
d = [(sys.maxsize, 0) for _ in range(N+1)]

for i in range(M):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))

dijk(1)

cnt = 0
result = []
for i in range(2, N+1):
    if d[i][0] != sys.maxsize:
        cnt += 1
        result.append((i, d[i][1]))

print(cnt)
for n, c, in result:
    print(n, c)