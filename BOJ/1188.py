import sys
input = sys.stdin.readline

M, N = map(int, input().split())

s = N * M

cnt = 0
while s > 0:
    s -= M
    if s % N == 0:
        continue
    cnt += 1
    # print(s, cnt)

print(cnt)
