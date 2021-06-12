#format(int, b) : 2진수
#format(int, o) : 8진수
#format(int, h) : 16진수

import sys
from collections import deque

input = sys.stdin.readline

q = deque()

#시작숫자
start = input()
end = input()

visit = [1000000 for i in range(1024)]

q.append((int(start, 2), 0))

while q:
    number, cnt = q.popleft()
    qtop = format(number, 'b')

    #현재 값이 목표값과 같으면 멈춤
    if int(qtop, 2) == int(end, 2):
        print(cnt)
        break
    
    if visit[number] <= cnt:
        continue
    else:
        visit[number] = cnt
    
    # 한자리 숫자 보수로 바꾸기 : 1 - 0으로 0은 1으로
    for i in range(1, len(qtop)):
        if qtop[i] == '0':
            tmp = qtop[0:i] + '1' + qtop[i+1:]
        else:
            tmp = qtop[0:i] + '0' + qtop[i+1:]

        q.append((int(tmp, 2), cnt + 1))

    # 현재수 + 1
    if number < 1023:
        q.append((number + 1, cnt + 1))

    # 현재수 - 1 
    if number > 0:
        q.append((number - 1, cnt + 1))
