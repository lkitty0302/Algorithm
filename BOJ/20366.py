import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

arr.sort()

result = sys.maxsize

for i in range(0, n - 3):
    for j in range(i + 3, n-1):
        left = i + 1
        right = j - 1
        
        #0이면 더이상 탐색할 필요 없음
        if result == 0:
            break

        
        while left <= right:
            snow1 = arr[i] + arr[j]
            snow2 = arr[left] + arr[right]

            result = min(result, abs(snow1 - snow2))

            if snow1 > snow2:
                left += 1
            else:
                right -= 1

print(result)

    

