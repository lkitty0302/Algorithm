import sys
input = sys.stdin.readline

# 오토마타 상태그래프
def next(char, state, cnt):
    if cnt == len(str):
        return state
    
    if char == "0":
        if state == 1:
            return 2
        elif state == 3:
            return 2
        elif state == 4:
            return 5
        elif state == 5:
            return 6
        elif state == 6:
            return 6
        elif state == 7:
            return 2
        elif state == 8:
            return 6
        elif state == 9:
            return 8
    else:
        if state == 1:
            return 4
        elif state == 2:
            return 3
        elif state == 3:
            return 4
        elif state == 6:
            return 7
        elif state == 7:
            return 9
        elif state == 8:
            return 1
        elif state == 9:
            return 9

    return 0

t = int(input())

for i in range(t):
    str = input()
    flag = 1
    cnt = 1
    for c in str:
        flag = next(c,flag, cnt)
        print(flag)
        cnt+=1
        if flag == 0:
            break
    
    if flag == 1 or flag == 3 or flag == 7 or flag == 9:
        print("YES")
    else:
        print("NO")