import sys
import heapq

input = sys.stdin.readline

pq = []

n = int(input())
table = []

for i in range(n):
    idx, s, e = map(int, input().split())

    heapq.heappush(pq, (s, e, idx))

for i in range(n):
    s, e, idx = heapq.heappop(pq)

    if len(table) == 0:
        heapq.heappush(table, (e, s, idx))
        continue
    
    te, ts, tidx = heapq.heappop(table)

    if te > s:
        heapq.heappush(table, (te, ts, tidx))
    
    heapq.heappush(table, (e, s, idx))

print(len(table))