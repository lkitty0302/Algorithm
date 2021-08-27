import sys
import heapq
input = sys.stdin.readline

N = int(input())

arr = [[]for _ in range(N)]
dq = []

for i in range(N):
    a, b = map(int, input().split())
    heapq.heappush(dq, (-a, b, i+1))

rq = []
result = []

a, b, c = heapq.heappop(dq)

deadline = -a
heapq.heappush(dq, (a, b, c))

while deadline > 0:
    while dq:
        d, r, idx = heapq.heappop(dq)
        if deadline > -d:
            #안돼는 경우
            heapq.heappush(dq, (d, r, idx))
            break
        heapq.heappush(rq, (-r, -d, idx))

    if len(rq) > 0:
        r, d, idx = heapq.heappop(rq)
        result.append((d, -r, idx))
    deadline -= 1

answer = 0
for i in range(len(result)):
    answer += result[i][1]

print(answer)
