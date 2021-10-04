import sys

input = sys.stdin.readline

n = int(input())

arr = [True for _ in range(n+1)]

for i in range(2, int(n**0.5)+1):
    cnt = 2
    t = i * cnt
    while t <= n:
        arr[t] = False
        cnt += 1
        t = i * cnt

table = [0]
sum = 0
for i in range(2, n+1):
    if arr[i] == True:
        sum += i
        table.append(sum)
print(table)
result = 0
left = 0
right = 1
sum = 0

while right < len(table):
    sum  = table[right] - table[left]

    if sum < n:
        right += 1
    elif sum > n:
        left += 1
    else:
        result += 1
        right += 1

print(result)