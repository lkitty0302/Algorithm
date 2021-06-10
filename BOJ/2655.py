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

# dp[0] = m[0][1]
for i in range(N):
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

# 5
# 25 1 4
# 4 1 6
# 9 1 3
# 16 1 5
# 1 1 2