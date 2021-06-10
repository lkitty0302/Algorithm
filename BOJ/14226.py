import sys
from collections import deque
# 저번에 python에서 queue를 왜 안쓰느냐라고 물어봐서 제가 Queue를 써봤습니다,,,
# 옛날에 c++로 이미 풀어봤던 문제라 
# 시간초과가 나면 안될 부분에서 시간초과가 나고, python3로 답을 출력해보면 특정 부분에서 정답이 다르다고 나옵니다.
# 접근 방법
# 

input = sys.stdin.readline

visit = [1000000 for _ in range(1002)]

s = int(input())

q = deque()

q.append((1, 0, 0))

while q:
    display, emo, time = q.popleft()

    # 출력하고자 하는 이모티콘의 갯수와 같으면 출력
    if display == s:
        break

    # 이전에 방문했을때가 시간이 더 적게들면 continue
    if visit[display] < time:
        continue

    #이모티콘 복사
    if display * 2 <= 1000:
        q.append((display, display, time + 1))

    # 디스플레이에 현재 클립보드에 복사된 이모티콘 붙혀넣기
    if display + emo <= 1000:
        q.append((display + emo, emo, time + 1))
        
    
    # 아모티콘하나 지우기
    if display > 0 :
        q.append((display - 1, emo, time + 1))
        
    if visit[display] > time + 1:
        visit[display] = time + 1
print(time)