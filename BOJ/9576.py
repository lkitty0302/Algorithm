import sys
# 그리디 알고리즘

case = int(input())

for t in range(case):
    n, m = map(int, input().split())

    arr = []
    check = [True for _ in range(n+1)]
    for i in range(m):
        a, b = map(int, input().split())
        arr.append((b, -a))
    
    arr.sort()
    # print(arr)
    result = 0
    cnt = 0
    for i in range(m):
        te, ts = arr[i]
        
        for j in range(-ts, te+1):
            # print("j : ", j)
            if check[j] == True:
                check[j] = False
                result += 1
                break

    print(result)
