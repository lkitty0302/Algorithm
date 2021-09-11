import sys
input = sys.stdin.readline
def fdic(name):
    global cnt
    if name in dict:
        idx = dict[name]
    else:
        dict[name] = cnt
        idx = cnt
        cnt += 1

    return idx

def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        table[a] = b
        result[b] += result[a]
        result[a] = 0
    return result[b]

def find(num):
    if table[num] == num:
        return num

    table[num] = find(table[num])
    return table[num]

t = int(input())

for i in range(t):
    dict = {}
    cnt = 0
    idx = 0

    n = int(input())
    table = [k for k in range(n*2)]
    result = [1 for _ in range(n*2)]

    for j in range(n):
        # dict
        name1, name2 = input().split()
        idx1 = fdic(name1)
        idx2 = fdic(name2)
        
        ans = union(idx1, idx2)
        # print(result)
            
        print(ans)
