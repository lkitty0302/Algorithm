import sys

input = sys.stdin.readline

def check(number):
    snum = str(number)

    for i in range(len(snum)):
        value = snum[i]

        if arr[int(value)] == False:
            return False

    return True

channel = int(input())

it = int(input())

arr = [True for _ in range(10)]

if it > 0:
    li = list(map(int, input().split()))

    for i in li:
        arr[i] = False


result = channel - 100

for i in range(1000001):
    tmp = check(i)

    if tmp == False:
        continue

    result = min(result, len(str(i)) + abs(channel - i))

print(result)