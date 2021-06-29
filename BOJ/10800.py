# 문제 포인트
# size별로 정렬해서 누적합을 이용하여 해결
# 색깔별 누적합을 저장하여 현재 누적합에서 겹치는 색 제거
# 같은 크기의 공은 --를 통해 해결

import sys
input = sys.stdin.readline
arr = []

N = int(input())

for i in range(N):
    color, size = map(int, input().split())
    arr.append((size, color, i))

# size를 기준으로 정렬
arr.sort()
ps = [0 for _ in range(N)]
cps = [0 for _ in range(200001)]

result = []

#크기가 같은 경우 가장 앞쪽의 idx를 저장
sidx = 0
# 누적합
sum = 0
for i in range(N):
    # 크기가 큰 경우 sidx를 하나씩 늘려가며 점수 추가(크기가 같은 경우 예외처리)
    while arr[sidx][0] < arr[i][0]:
        sum += arr[sidx][0]
        # 색깔별 누적합
        cps[arr[sidx][1]] += arr[sidx][0]
        
        sidx += 1
    
    result.append((arr[i][2], sum - cps[arr[i][1]]))

result.sort()

for i in range(N):
    print(result[i][1])