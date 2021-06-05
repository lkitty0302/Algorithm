# strip([char]), lstrip([char]), rstrip([char]) : 지정한 char값 제거
# strip : 양쪽, lstrip : 왼쪽, rstrip : 오른쪽
# print(" ",end = '\n') : 기본형
# end = '' : print 끝 줄바꿈을 하지 않겠다는 의미

from collections import deque
import heapq
import sys
from typing import Deque

input = sys.stdin.readline

T = int(input())

for i in range(T):
    str = list(input().rstrip())

    num_cnt = int(input())

    num_list = input().rstrip().strip('[]').split(',')

    #처음은 앞에서부터 삭제
    flag = False
    result = True
    q = deque()

    for j in num_list:
        if j != '':
            q.append(j)

    for j in str:
        if j == 'R':
            flag = not(flag)
        else:
            #밖에서 q의 길이 체크를 하면 큐가 비어있는 상태에서 R연산시 error출력
            if len(q) == 0:
                result = False
                break

            if flag:
                q.pop()
            else:
                q.popleft()
    # [1,2,3,4]
    # 정답 출력
   
    if result:
        print("[", end = '')
        for i in range(len(q)):
            if flag:
                print(q.pop(), end = '')
            else:
                print(q.popleft(), end = '')
            
            if len(q) != 0:
                print(",", end = '')
        print(']')

    else:
        print("error")