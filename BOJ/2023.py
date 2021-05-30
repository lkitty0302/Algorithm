import sys

input = sys.stdin.readline

# 첫째자리는 무조건 소수인 수가 들어가야하고
# 두번째 자리 부터는 홀수인 1, 3, 7, 9가 들어가서 홀수인지 판별한다(마지막 수가 5인경우 무조건 5로 나누어 떨어지기 때문에 제외)

first = [2, 3, 5, 7]
next = [1, 3, 7, 9]

def isPrime(num):
    for i in range(2, num//2 + 1):
        if num % i == 0:
            return False
    return True

def dfs(num, now):
    if isPrime(num):
        if now == n:
            print(num)
            return

        for i in next:
            dfs(num * 10 + i, now+1)
   

n = int(input())

for i in range(4):
    dfs(first[i], 1)