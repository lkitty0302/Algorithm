import sys
import heapq

input = sys.stdin.readline

N, L = map(int, input().split())

arr = list(map(int, input().split()))

result = []
q = []

idx = 0
v = arr[0]

for i in range(N):
    if v > arr[i]:
        idx = i
        v = arr[i]
    else:
        heapq.heappush(q, (arr[i], i))
        
    n = i - L + 1

    if n <= idx:
        result.append(v)
    else:
        while True:
            v, idx = heapq.heappop(q)
            if idx >= n:
                break
        result.append(v)

print(*result)
    
