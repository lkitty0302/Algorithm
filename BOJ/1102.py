import sys
input = sys.stdin.readline

n = int(input())

arr = [[] for i in range(n+1)]

for i in range(1, n+1):
    arr[i] = list(map(int, input().split()))

visit = [False for i in range(n+1)]
result = [100000000 for i in range(n+1)]

s = input()
cnt = 0

bit = 0

for i in range(n):
    if s[i] == 'Y':
        cnt += 1
        bit |= 1<<i

p = int(input())

