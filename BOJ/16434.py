import sys
input = sys.stdin.readline
# 틀린 이유
N, attack = map(int, input().split())
hp = 1
arr = []

for i in range(N):
    tmp = list(map(int, input().split()))

    #arr[0] == 1 : 공격력이 arr[1]이고 생명력이 arr[2]인 몬스터가 존재하는 방
    #arr[0] == 2 : 공격력이 arr[1]만큼 증가하고 arr[2]만큼 생명력을 증가시켜주는 방
    arr.append(tmp)
max = 0

for i in range(N):
    if arr[i][0] == 1:
        tmp = arr[i][2] // attack
        tmp *= arr[i][1]
        # print(tmp)
        flag = arr[i][2] % attack
        if flag == 0:
            tmp -= arr[i][1]
        hp += tmp
        # print(tmp)
    else:
        attack += arr[i][1]

        hp -= arr[i][2]

        if hp < 1:
            hp = 1
    if max < hp:
            max = hp
print(max)