import sys

input = sys.stdin.readline

#가로 : x보다 오른쪽
#세로 : y보다 위쪽(floor배열에서 y보다 큰 층수 - left를 y로 잡고/ floor[y]보다 작은수가 나오면 오른쪽을 옮긴다)

n, q = map(int, input().split())

floor = [0 for _ in range(250001)]

arr = list(map(int, input().split()))
for i in range(1, n+1):
    floor[i] = arr[i-1]

xy = []
for i in range(q):
    x, y = map(int, input().split())
    
    left = y
    right = n

    while left <= right:
        mid = (left + right) // 2
        if floor[mid] < x:
            right = mid - 1
        else:
            left = mid + 1
    # print(floor[y],(x-1) , floor[y] - (x-1))
    # print(right, y, right - (y))
    # print(floor[y]-(x-1) + right - (y))
    if floor[y]-(x-1) + right - (y) > 0:
        xy.append(floor[y]-(x-1) + right - (y))
    else:
        xy.append(0)

for i in range(len(xy)):    
    print(xy[i])


# 3 11
# 3 3 2
# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3
# 3 1
# 3 2
# 4 1
# 4 2
# 3 3