import sys

input = sys.stdin.readline

a = []
b = []

n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    a.append((x + y))
    b.append((x - y))

a.sort()
b.sort()

print(max(abs(a[0] - a[-1]), abs(b[0] - b[-1])))
