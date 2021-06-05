import sys

input = sys.stdin.readline

n, d, k, c = map(int, input().split())

arr = [int(input()) for _ in range(n)]
check = [0 for _ in range(3001)]

result = 0
left = 0
right = 0
cnt = 1
s = set()

s.add(arr[left])
check[arr[left]] += 1

while True:
    right = (right + 1) % n
    s.add(arr[right])
    check[arr[right]] += 1
    cnt += 1

    if cnt == k :
        #현재 집합에 쿠폰을 사용할 접시 포함 여부 확인
        if c in s:
            result = max(result, len(s))
        else:
            result = max(result, len(s) + 1)
            
        check[arr[left]] -= 1

        if check[arr[left]] == 0:
            s.remove(arr[left])
        
        left = (left + 1) % n 
        s.add(arr[left])
        cnt -= 1

        if left == 0 : break

print(result)