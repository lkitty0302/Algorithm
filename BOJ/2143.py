import sys
from collections import Counter

t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

pa = []
pb = []

for i in range(n):
    sum = 0
    for j in range(i, n):
        sum += a[j]
        pa.append(sum)
        

for i in range(m):
    sum = 0
    for j in range(i, m):
        sum += b[j]
        pb.append(sum)

pa.sort()
pb.sort()

arr = Counter(pb)

answer = 0

for i in pa:
    answer += arr[t-i]

print(answer)