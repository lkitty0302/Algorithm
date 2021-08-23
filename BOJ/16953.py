import sys
from collections import deque
input = sys.stdin.readline

a, b = map(int, input().split())

q = deque()
q.append((a, 1))

# visit = [sys.maxsize for _ in range(b+1)]
result = sys.maxsize

while q:
    num, cnt = q.popleft()

    if num == b:
        # visit[num] = cnt
        result = cnt
        break

    # if num <= b and visit[num] > cnt:
    # visit[num] = cnt
    if num <= b:
        q.append((num * 2, cnt + 1))
        q.append((((num * 10) + 1), cnt + 1))

if result == sys.maxsize:
    result = -1

print(result)