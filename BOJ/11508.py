import sys
input = sys.stdin.readline

N = int(input())

arr = []
for i in range(N):
    arr.append(-int(input()))

arr.sort()

result = 0

for i in range(N):
    if (i+1) % 3 == 0:
        continue
    result += arr[i]

print(-result)