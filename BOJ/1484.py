import sys
input = sys.stdin.readline

num = int(input())

left = 1
right = 2

result = []
while left < right:
    
    tmp = right**2 - left ** 2
    print(left, right, tmp)

    if tmp == num:
        result.append(right)
        right += 1
        continue

    if tmp < num:
        right += 1
    else:
        left += 1

if len(result) == 0:
    print(-1)

for i in result:
    print(i)
