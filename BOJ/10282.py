import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    q = []
    data = [sys.maxsize for _ in range(n+1)]
    visit = [False for _ in range(n+1)]

    heapq.heappush(q, (0, start))
    data[start] = 0
    visit[start] = True
    
    while q:
        time, f = heapq.heappop(q)

        for tmp, next in graph[f]:
            if tmp + time < data[next]:
                data[next] = tmp + time
                heapq.heappush(q, (tmp + time, next))

    return data

T = int(input())

q = []

for t in range(T):
    n, d, c = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    
    for i in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((s, a))


    result = dijkstra(c)

    sum = 0
    cnt = 0
    for i in range(n+1):
        if result[i] != sys.maxsize :
            cnt += 1
            if result[i] > sum:
                sum = result[i]

    print(cnt, sum)