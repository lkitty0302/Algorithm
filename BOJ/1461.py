import sys
import heapq
input = sys.stdin.readline

def shortArr(arr):
    global result
    cnt = 0
    while arr:
        value = heapq.heappop(arr)
        if cnt % M == 0:
            result += (value * 2)
        cnt += 1

    return

def longArr(arr):
    global result
    #돌아오지 않아도 되는 경우
    result += heapq.heappop(arr)
    for _ in range(M-1):
        if len(arr) == 0:
            break
        heapq.heappop(arr)

    cnt = 0
    while arr:
        value = heapq.heappop(arr)
        if cnt % M == 0:
            result += (value * 2)
        cnt += 1
    return

N, M = map(int, input().split())

arr = list(map(int, input().split()))

Min = []
Max = []

tmp = 0
for i in arr:
    if i < 0:
        heapq.heappush(Min, i)
        if abs(tmp) < abs(i):
            tmp = i
    else:
        heapq.heappush(Max, -i)
        if abs(tmp) < i:
            tmp = i

result = 0
if tmp < 0:
    shortArr(Max)
    longArr(Min)
        
else:
    shortArr(Min)
    longArr(Max)

print(abs(result))