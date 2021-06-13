# 주어진 Ai ~ AN 수열은 순서를 변경할 수 없음
# 주어진 덧셈, 뺄셈, 곱셈, 나눗셈 연산의 개수(최대 N-1개)를 활용하여 만들 수 있는 숫자의 최대값과 최소값을 구하자

# 접근 방법
# 숫자의 순서는 바꿀 수 없기 때문에 연산자를 바꿔가며 연산한다
# 2 <= N <= 11이기 때문에 연산자는 최대 10개가 주어진다
# 따라서 최악의 경우 시간복잡도는 (N-1)! = 10! = 약 360만
# 1억 미만이기 때문에 완전탐색으로 풀이 가능

import sys
input = sys.stdin.readline

def dfs(number, cnt):
    # print(number)
    global mm
    global minn

    if N == cnt:
        if number > mm:
            mm = number
        if number < minn:
            minn = number
        return
    
    for i in range(4):
        if op[i] > 0:
            op[i] -= 1

            if i == 0:
                dfs(int(number + lista[cnt]), cnt + 1)
            elif i == 1:
                dfs(int(number - lista[cnt]), cnt + 1)
            elif i == 2:
                dfs(int(number * lista[cnt]), cnt + 1)
            elif i == 3:
                dfs(int(number / lista[cnt]), cnt + 1)

            op[i] += 1
    return

N = int(input())

lista = list(map(int, input().split()))

op = list(map(int, input().split()))

mm = -1000000001
minn = 1000000001

dfs(lista[0], 1)

print(mm)
print(minn)