import sys
input = sys.stdin.readline

# a + b + c = d를 만족하는 수의 갯수를 찾는다
# a + b + c = d를 a + b = d - c로 생각해보면 
# d 이전에 나왔던 조합 중에서 a + b의 결과가 존재한다면 좋은 수라고 할 수 있다.
# 따라서 N^2만에 해결 가능

n = int(input())
s = set()

arr = list(map(int, input().split()))

result = 0
s.add(arr[0] + arr[0])

for i in range(1, n):
    for j in range(i):
        if arr[i] - arr[j] in s:
            result += 1
            break
    
    for j in range(i+1):
        s.add(arr[i] + arr[j])

print(result)