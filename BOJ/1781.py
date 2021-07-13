import sys
import heapq
input = sys.stdin.readline

N = int(input())

arr = [[]for _ in range(N)]
dq = []
rq = []

# 0 : 데드라인, 1 : 컵라면 수
for i in range(N):
    a, b = map(int, input().split())
    # heapq.heappush(dq, (a, b, i+1))
    heapq.heappush(rq, (-b, a, i+1))


result = []

# a, b, c = heapq.heappop(dq)

deadline = 1
# heapq.heappush(dq, (a, b, c))
# print(a, b, c)
while deadline < N:
    # while dq:
    #     d, r, idx = heapq.heappop(dq)
    #     print(deadline, d, r, idx)
    #     if deadline > d:
    #         #안되는 경우
    #         heapq.heappush(dq, (d, r, idx))
    #         break
    #     heapq.heappush(rq, (-r, d, idx))
    print(rq)

    if len(rq) > 0:
        r, d, idx = heapq.heappop(rq)
        if d >= deadline:
            result.append((d, -r, idx))
    deadline += 1
    
    print("result", result)

answer = 0
print(result)
for i in range(len(result)):
    answer += result[i][1]
    print(result[i][2])

print(answer)

# 반례
# 5
# 1 7
# 1 10
# 2 20
# 2 30
# 3 40

# 7
# 1 6
# 1 7
# 3 2
# 3 1
# 2 4
# 2 5
# 6 1

#1 1 2 2 3 3 6
#