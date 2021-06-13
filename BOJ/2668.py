import sys

input = sys.stdin.readline

result = []

def dfs(start, finish, visit):

    if start == finish:
        result.append(start)
        return True

    if visit[finish] == True:
        return False
    visit[finish] = True
    dfs(start, arr[finish], visit)

n = int(input())

arr = [0 for _ in range(n+1)]
visit = [False for _ in range(n+1)]

for i in range(1, n+1):
    arr[i] = int(input())

for i in range(1, n+1):
    visit[i] = True
    dfs(i, arr[i], visit)
    visit = [False for _ in range(n+1)]

print(len(result))

for i in result:
    print(i)
