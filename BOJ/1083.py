import sys

input = sys.stdin.readline

target = 0

n = int(input())

arr = list(map(int, input().split()))

s = int(input())

while s > 0 and target <= len(arr)-1:
    # arr[target] ~ arr[target + s]번중 가장 큰 수를 앞으로 가져온다.
    # 횟수는 가장 큰수의 idx - target
    # 만약 현재 arr[target]이 가장 큰수라면 더할필요없이 target만 변경
    m = target

    for i in range(s+1):
        if target + i >= len(arr):
            break
        # print(target, m, s)
        if arr[target + i] > arr[m]:
            m = target + i
        
    s -= m - target

    # print(m, target)
    if m == target:
        target += 1
        continue

    arr.insert(target, arr[m])
    del arr[m+1]
    target += 1

print(*arr)

# 1 2 3 4 5 6 7 8 9 10
# 2 1 3 ~
# 2 3 1 ~
# 3 2 1 ~
# 3 2 4 1 ~
# 3 4 2 1 ~

# 5
# 20 3 4 5 6  
# 5

# 20 6 5 3 4