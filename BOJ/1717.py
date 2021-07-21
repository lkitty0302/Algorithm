import sys
input = sys.stdin.readline

def union(a, b):
    a = find(a)
    b = find(b)

    if a > b:
        arr[a] = b
    else:
        arr[b] = a
    return

def find(num):
    if arr[num] == num:
        return num
    num = find(arr[num])
    return num

n, m = map(int, input().split())

arr = [i for i in range(n+1)]
print(arr)

for i in range(m):
    op, a, b = map(int, input().split())

    if op:
        if find(a) == find(b):
            print("yes")
        else:
            print("no")
    else:
        union(a, b)
    



# 7 8
# 0 1 3
# 1 1 7
# 0 7 6
# 1 7 1
# 0 3 7
# 0 4 2
# 0 1 1
# 1 1 1
# 0 7 2
# 0 6 3