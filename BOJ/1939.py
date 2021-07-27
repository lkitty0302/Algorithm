import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    global n
    q = []

    heapq.heappush(q, (-1000000001, start))

    while q:
        value, node = heapq.heappop(q)
        # print(value, node)

        if cost[node] > -value:
            continue
        
        for i in range(len(graph[node])):
            next_node, nvalue = graph[node][i]
            nvalue = min(nvalue, -value)

            if cost[next_node] < nvalue:
                cost[next_node] = nvalue
                heapq.heappush(q, (-nvalue, next_node))

    return

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
cost = [0 for _ in range(n+1)]
visit = [False for _ in range(n+1)]

for i in range(m):
    s, e, v = map(int, input().split())

    graph[s].append((e, v))
    graph[e].append((s, v))

# print(graph)
p1, p2 = map(int, input().split())

cost[p1] = 100000001
dijkstra(p1)

print(cost[p2])

# 8 12
# 1 2 1
# 1 2 4
# 1 3 4
# 1 3 2
# 3 4 2
# 2 5 4
# 2 4 3
# 5 7 2
# 4 8 2
# 4 6 4
# 6 8 3
# 7 8 3
# 1 8