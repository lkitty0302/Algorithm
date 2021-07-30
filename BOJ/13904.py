import sys
import heapq
input = sys.stdin.readline

N = int(input())

dq = []
sq = []

for i in range(N):
    d, s = map(int, input().split())
    heapq.heappush(dq, (-d, s))

a, b = heapq.heappop(dq)
dline = -a

heapq.heappush(dq, (a, b))

result = 0
while dline > 0:
    while dq:
        d, s = heapq.heappop(dq)
        if dline > -d:
            heapq.heappush(dq, (d, s))
            break
        heapq.heappush(sq, (-s, -d))
    
    if len(sq) > 0:
        s, d = heapq.heappop(sq)
        result += -s

    dline -= 1
    
print(result)