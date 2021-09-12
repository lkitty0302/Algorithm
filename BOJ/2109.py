import sys
import heapq

input = sys.stdin.readline

n = int(input())

pq = []
rq = []

for i in range(n):
    p, d = map(int, input().split())
    heapq.heappush(pq, (-d, p))

deadline = 0
if len(pq) > 0:
    deadline = -pq[0][0]

result = 0
while deadline > 0:
    while pq:
        d, p = heapq.heappop(pq)
        if -d < deadline:
            heapq.heappush(pq, (d, p))
            break

        heapq.heappush(rq, -p)
    
    if len(rq) > 0:
        c = heapq.heappop(rq)
        result += c
    
    deadline -= 1

print(-result)

