import sys
input = sys.stdin.readline
#CCW알고리즈으로 해결하는 문제

def solv(x, y):
    return (arr[y] - arr[x])/(y-x)

n = int(input())

arr = list(map(int, input().split()))
result = [0 for _ in range(n)]

for i in range(n-1):
    d = 0
    cur = 0
    for j in range(i + 1, n):
        d= solv(i, j)
        if j - 1 == i or cur < d:
            cur = d
            result[i] += 1
            result[j] += 1

ans = 0
for i in result:
    if ans < i:
        ans = i

print(ans)

