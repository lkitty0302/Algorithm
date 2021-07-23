import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
check = [0 for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    check[b] += 1

q = []
result = []

for i in range(1, n+1):
    if check[i] == 0:
        heapq.heappush(q, i)

for i in range(1, n+1):
        while q:
            num = heapq.heappop(q)
            check[num] = -1
            result.append(num)

            for j in range(len(graph[num])):
                check[graph[num][j]] -= 1
                if graph[num][j] != 0 and check[graph[num][j]] == 0:
                    heapq.heappush(q, graph[num][j])
                    graph[num][j] = 0

print(*result)