import sys
import heapq


input = sys.stdin.readline

n, k = map(int, input().split())

result = 0
mv = []
mw = []

bag = [0 for _ in range(k)]

for i in range(n):
    m, v = map(int, input().split())
    heapq.heappush(mv, (m, v))

for i in range(k):
    bag[i] = int(input())

bag.sort()

for i in bag:
    while True:
        if len(mv) == 0:
            break
        
        tm, tv = heapq.heappop(mv)

        if i < tm :
            heapq.heappush(mv, (tm, tv))
            break
        
        heapq.heappush(mw, (-tv, tm))

    maxv, maxw = heapq.heappop(mw)

    result -= maxv

print(result)