import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

gr = [[] for _ in range(N+1)]
visit = [0 for _ in range(N+1)]

q = deque()

for i in range(M):
    tmp = list(map(int, input().split()))
    for j in range(1, tmp[0]):
        gr[tmp[j]].append(tmp[j+1])
        visit[tmp[j+1]] += 1

for i in range(1, len(visit)):
    if visit[i] == 0:
        q.append(i)

result = []

while q:

    idx = q.popleft()
    result.append(idx)

    for j in range(len(gr[idx])):
        visit[gr[idx][j]] -= 1
        if visit[gr[idx][j]] == 0:
            q.append(gr[idx][j])
    

if len(result) == N:
    for i in range(len(result)):
        print(result[i])
else:
    print(0)