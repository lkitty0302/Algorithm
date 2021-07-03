import sys
input = sys.stdin.readline

def check(str):
    if 'a' <= str <= 'z':
        return ord(str.upper()) - ord('A') + 26
    else:
        return ord(str) - ord('A')

g, s = map(int, input().split())

W = input()
S = input()

st = [0 for i in range(52)]
result = [0 for i in range(52)]

answer = 0
cnt = 0
for i in range(g):
    st[check(W[i])] += 1

for i in range(s):
    result[check(S[i])] += 1
    cnt += 1
    if cnt == g:
        if result == st:
            answer += 1
        result[check(S[i-g+1])] -= 1
        cnt -=1

print(answer)