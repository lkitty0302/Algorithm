import sys
input = sys.stdin.readline

n = int(input())

now = list(map(int, input().split()))
tab = list(map(int, input().split()))

result = 0

for i in range(n):
    s = i
    e = i
    #flag : 0 - 감소
    #flag : 1 - 증가
    flag = 0
    if now[i] == tab[i]:
        continue
    
    if now[i] - tab[i] < 0:
        flag = 1
    
    for j in range(s, n):
        if now[j] - tab[j] < 0 and flag == 1:
            e += 1
        elif now[j] - tab[j] > 0 and flag == 0:
            e += 1
        else:
            break
    
    while now[i] != tab[i]:
        for j in range(s, e):
            if now[j] == tab[j]:
                    break

            if flag == 1:
                now[j] += 1
            else:
                now[j] -= 1

        result += 1

print(result)


