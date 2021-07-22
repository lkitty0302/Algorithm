import sys
input = sys.stdin.readline

def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return -1
    if a > b:
        table[a] = table[b]
    else:
        table[b] = table[a]
    
    return 0

def find(num):
    if table[num] == num:
        return num
    
    table[num] = find(table[num])
    return table[num]

n, m = map(int, input().split())

table = [i for i in range(n)]

result = 0
for i in range(m):
    flag = 0
    a, b = map(int, input().split())
    flag = union(a, b)
    if flag == -1:
        result = i+1
        break

print(result)