import sys
input = sys.stdin.readline

n, k = map(int, input().split())
temp = n
cnt = 0
result = 0

while True:
    cnt = 0
    temp = n
    while temp > 0:
        if temp % 2 == 1:
            cnt += 1
    
        temp = temp // 2

    if cnt <= k:
        break
    else:
        n += 1
        result += 1

print(result)