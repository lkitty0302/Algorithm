# 1 <= N <= 19
# 각 숫자 앞 연산자를 하나의 범위로 설정하여 DFS(완전탐색)
# ex) 3 + 5 * 7 - 6 = ['+3', '+5', '*7', '-6']

import sys

input = sys.stdin.readline

N = int(input())

strr = input()

M = -pow(2,32)

arr = []
def cal(v1, v2):
    result = 0
    op1 = v1[0]
    op2 = v2[0]

    num1 = int(v1[1:])
    num2 = int(v2[1:])

    if op2 == '+':
        result = num1 + num2
    elif op2 == '-':
        result = num1 - num2
    elif op2 == '*':
        result = num1 * num2
    elif op2 == '/':
        result = num1 / num2

    return op1 + str(result)

def dfs(idx, value):
    global M
    tmp = int(value[1:])
    if idx >= len(arr)-1:
        if M < tmp:
            M = tmp
        return
    
    dfs(idx + 1, cal(value, arr[idx+1]))

    if idx + 2 <= len(arr)-1:
        dfs(idx + 2, cal(value, cal(arr[idx+1], arr[idx+2])))

    return

for i in range(int(N/2+1)):
    if i == 0:
        tmp = '+' + strr[0]
        arr.append(tmp)
        continue
    arr.append(strr[i*2-1] + strr[i*2])

dfs(0, arr[0])

print(M)