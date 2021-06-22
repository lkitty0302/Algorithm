# 두개의 heap을 사용하여 해결
import sys
import heapq

input = sys.stdin.readline

N = int(input())

minq = []
maxq = []

result = []

for i in range(N):
    tmp = int(input())

    if len(minq) < len(maxq) :
        heapq.heappush(minq, tmp)
    else:
        heapq.heappush(maxq, -tmp)

    if len(maxq) > 0 and len(minq) > 0:
        if -maxq[0] > minq[0]:
            M = -heapq.heappop(maxq)
            m = heapq.heappop(minq)

            heapq.heappush(maxq, -m)
            heapq.heappush(minq, M)

    print(-maxq[0])

