# 이 문제는 밑변과 무게 2개의 변수가 있기 때문에 둘 중 하나를 기준으로 정렬하여 해결
# 본인은 밑변을 오름차순으로 정렬하여 문제를 해결
# 0. 데이터를 입력받을때 각 벽돌의 index를 함께 저장
# 1. 밑변(무게)를 기준으로 오름차순 정렬
# 2. 바닥에 놓은 벽돌을 기준으로 무게와 밑면이 작은 벽돌이 있는 경우 높이를 더해줌
# 3. 높이가 저장된 배열에서 가장 큰 값과 큰 값을 가지는 index를 저장
# 4. index부터 저장된 높이와 비교하면서 index 추출
# 5. 밑면(무게)가 작은것부터 출력하기 때문에 역으로 출력

import sys

input = sys.stdin.readline

N = int(input())

m = []

for i in range(1, N+1):
    a, b, w = map(int, input().split())
    m.append((a, b, w, i))

# 밑면 기준으로 오름차순 정렬
m.sort()

dp = [0 for _ in range(N)]
idx = []

for i in range(N):
    #실패요인
    dp[i] = m[i][1]
    # 밑면을 기준으로 오름차순 정렬을 했기 때문에, 밑면 기준 0~i까지가 쌓을 수 있는 상자이므로
    # 밑면 기준 쌓을 수 있는 상자를 대상으로 무게를 확인
    for j in range(i+1):
        #현재 바닥에 있는 상자(i)보다 확인하고 있는 상자(j)의 무게가 작으면 dp[i]배열에 최대 높이 저장
        if m[i][2] > m[j][2]:
            dp[i] = max(dp[i], dp[j] + m[i][1])

# dp에 저장된 높이 중 가장 높은 값을 가지는 값 추출
h = max(dp)
# 가장 높은 값을 가진 dp의 idx 추출
max_idx = dp.index(h)

# index찾기
while max_idx >= 0:
    if dp[max_idx] == h:
        idx.append(m[max_idx][3])
        h -= m[max_idx][1]
    max_idx -= 1

# 정답 출력
print(len(idx))
for i in range(1, len(idx)+1):
    print(idx[-i])
