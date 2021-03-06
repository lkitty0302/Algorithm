# 접근 방법
# 음의 간선이 없고 최단 거리를 구하는 문제이므로 다익스트라로 해결
# 정점(v1, v2)를 반드시 방문해야 하기 때문에
# 1. 시작지점 - v1 - v2 - 도착
# 2. 시작지점 - v2 - v1 - 도찰
# 위 두가지 경우 중 짧은 거리를 정답으로 출력

import heapq
import sys
# python에서 반복문으로 input받을 때 많은 시간이 걸리기 때문에 아래 코드로 input시간 단축
input = sys.stdin.readline

def dijkstra(st, end):
    visit = [sys.maxsize for i in range(n+1)]
    visit[st] = 0
    pq = []
    
    heapq.heappush(pq, (0,st))
    
    while pq:
        dist, node = heapq.heappop(pq)
        
        for tmpn, tmpd in arr[node]:
            d = dist + tmpd
            if d < visit[tmpn]:
                visit[tmpn] = d
                heapq.heappush(pq, (d, tmpn))
                
    return visit[end]

n, m = input().split()

n = int(n)
m = int(m)

arr = [[] for i in range(n+1)]

for i in range(m):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))

v1, v2 = map(int, input().split())

d1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
d2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)

result = min(d1, d2)

if(result >= sys.maxsize):
    print(-1)
else:
    print(result)
    