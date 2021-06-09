import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

st = []
result = [-1 for _ in range(n)]
st.append((arr[0], 0))

for i in range(1, n):
    while len(st) != 0 and st[-1][0] < arr[i]:
        v, idx = st.pop()
        result[idx] = arr[i]
    
    st.append((arr[i], i))

# while len(st) != 0:
#     t, idx = st.pop()
#     result[idx] = t

print(*result)