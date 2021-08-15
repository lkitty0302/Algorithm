import sys
input = sys.stdin.readline

# 이분탐색을 통해 드래곤 앤 던전 문제를 해결할 수 있다.
# 1개의 방에서 최대 공격력과 체력을 가진 몬스터가 있는 방에서 탈출하기 위해 필요한 용사의 체력 : 999999000001
# n개의 방이 있을때 필요한 용사의 최대 체력 : 999999000001 * n
# 따라서 용사의 최대 체력을 right로, 1을 left로 잡아서 이분탐색을 통해 문제를 해결


def binary(hp):
    global N
    thp = hp
    at = attack

    for i in range(N):
        if rooms[i][0] == 1:
            tmp = (rooms[i][2] // at) * rooms[i][1]
            
            #만약 나누어 떨어진다면 한대 덜 맞기 때문에 공격력 만큼 감소
            if rooms[i][2] % at == 0:
                tmp -= rooms[i][1]

            thp -= tmp
        else:
            at += rooms[i][1]
            #용사에게 필요한 maxHP를 구하되 최소 maxHP를 구해야 하기 때문에 현재 hp와 mid값 중 작은 값을 선택
            thp = min(thp + rooms[i][2], hp)
        # print(thp)

        if thp < 1:
            return False

    # print("end")
    return True

N, attack = map(int, input().split())

rooms = []

for i in range(N):
    rooms.append(list(map(int, input().split())))

right = 999999000001 * N
left = 1

while left <= right:
    mid = (left + right) // 2
    # print(mid)
    if binary(mid):
        # print("r")
        right = mid - 1
    else:
        # print("l")
        left = mid + 1
        
print(left)

