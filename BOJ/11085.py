import sys
import heapq
input = sys.stdin.readline

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        g[b] = a
    else:
        g[a] = b
    return

def find(a):
    if g[a] != a:
        return find(g[a])
    return a

p, w = map(int, input().split())
c, v = map(int, input().split())

g = [i for i in range(p+1)]

pq = []

for i in range(w):
    n, e, width = map(int, input().split())
    heapq.heappush(pq, (-width, n, e))

while pq:
    cost, start, end = heapq.heappop(pq)
    cost = -cost
    union(start, end)
    
    if find(c) == find(v):
        result = cost
        break


print(result)
    
    
