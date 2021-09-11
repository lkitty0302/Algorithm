import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

if n > 2:
    a = 0
    x = arr[1] - arr[0]
    y = arr[2] - arr[1]
    if x != 0 : a = y//x
    b = arr[1] - (a * arr[0])

    result = int((arr[n-1] * a) + b)

    for i in range(n-1):
        if arr[i+1] != (arr[i] * a) + b:
            result = "B"
            break

if n == 1:
    print("A")
elif n == 2:
    if arr[0] == arr[1]:
        print(arr[0])
    else:
        print("A")
else:
    print(result)

