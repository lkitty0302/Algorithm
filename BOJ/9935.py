import sys
input = sys.stdin.readline

# 스택을 이용해서 주어진 문자열s에서 비교대상 문자열 c와 비교한다.
# 여기서 핵심은 스택에 저장할때 비교할 문자열의 count와 함께 저장한다는것

s = input().rstrip()
c = input().rstrip()

st = []

top = -1
cnt = 0

for i in range(len(s)):
    if s[i] == c[cnt]:
        cnt += 1
    elif s[i] == c[0]:
        cnt = 1
    else:
        cnt = 0
    
    st.append((s[i], cnt))
    top += 1
    if cnt == len(c):
        for j in range(len(c)):
            st.pop()
            top -= 1
    
    if len(st) == 0:
        cnt = 0
    else:
        cnt = st[top][1]

result = ""

if len(st) == 0:
    print("FRULA")
else:
    for st, cnt in st:
        result += st

print(result)