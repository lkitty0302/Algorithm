import sys

input = sys.stdin.readline

# 덧셈의 절댓값이 가장 작은 수가 정답

# 투포인터를 사용해서 해결할 수 있다. 
# left를 0으로, right를 n-1로 초기화 하고 시작한다.
# 오름차순으로 정렬하여 사용한다.
# -6 -5 -4 -3 -2 -1 0 1 1 2 3 100000 2000000 ...

minerArr = []
plusArr = []


n = int(input())

arr = list(map(int, input().split()))

arr.sort()
a, b, max_num = 0, 0, sys.maxsize

left = 0
right = n-1
while left < right:
    if max_num >= abs(arr[left] + arr[right]):
        max_num = abs(arr[left] + arr[right])
        a = arr[left]
        b = arr[right]
    
    if max_num == 0:
        break
    # 현재 포인터가 가리키고 있는 값의 합이 0보다 크면 right를 줄여서 값을 줄여주고
    # 0보다 작으면 left를 옮겨 값을 키워준다
    if 0 < arr[left] + arr[right]:
        right -= 1
    else:
        left += 1

print(a, b)