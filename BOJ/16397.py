# Created on iPad.
import sys
from collections import deque

input = sys.stdin.readline

N, T, G = map(int, input().split())

visit = [False for _ in range(100001)]

q = deque()
q.append((N, 0))
visit[N] = True

answer = -1

while q :
  nvalue, ncnt = q.popleft()
  
  if ncnt > T :
    break
  
  if nvalue == G :
    answer = ncnt
    break

  result = nvalue + 1

  if -1 < result < 100000 and visit[result] == False:
    visit[result] = True
    q.append((result, ncnt + 1))

  tmp = str(nvalue * 2)

  k = len(tmp)

  result = int(tmp) - 10 ** (k-1)

	# 0일경우 한자리로 인식해서 10 ** -1이 나올 수 있기 때문에 0보다 작은 수는 큐에 넣지 않도록 처리
  if -1 < nvalue * 2 < 100000 and visit[result] == False:
    visit[result] = True
    q.append((result, ncnt + 1))  
    
if answer == -1 :
  print("ANG")
else :
  print(answer)