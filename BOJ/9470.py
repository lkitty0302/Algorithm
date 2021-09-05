import sys
from collections import deque
from types import coroutine
# 노드는 강이 시작하거나 합쳐지거나 바다가 시작하는 곳이고 간선이 강이 흐르는 방향을 나타냅니다.
# 보면 노드로 들어오는 간선이 없는 경우를 1로 두고 아래로 내려갈수록 순서가 커지는데 
# 이전 강 번호 i의 갯수가 2 이상이면 i+1, 아니라면 i그대로 내려온다는 조건이 있습니다.
# 뭔가 들어오는 간선이 없고 순서가 정해져있어서 위상정렬으로 풀 수 있다고 생각해서 위상정렬로 풀었습니다

def topological_sort():
    q = deque()
    count = [[] for _ in range(m+1)]
    count[0].append(1)
    #강의 번호 순서(정답)를 저장하는 배열
    result = [0 for _ in range(m+1)]

    #input이 없는 노드를 큐에 넣어줌
    for i in range(1, m+1):
        if insert[i] == 0:
            q.append((i, 1))
            count[i].append(-1)

    #q에 아무것도 없을때까지 반복
    while q:
        node, cnt = q.popleft()
        result[node] = cnt
        print(count)
        for j in range(len(table[node])):
            insert[table[node][j]] -= 1
            
            count[table[node][j]].append(-cnt)
            #들어오는 간선의 갯수가 없는 경우 
            if insert[table[node][j]] == 0:
                count[table[node][j]].sort()
                nnode = count[table[node][j]]
                # 
                if len(nnode) > 1 and nnode[0] == nnode[1]:
                    q.append((table[node][j], (-nnode[0]) + 1))
                else:
                    q.append((table[node][j], (-nnode[0])))
    # 
    return max(result)

input = sys.stdin.readline

tc = int(input())

for i in range(1, tc+1):
    k, m, p = map(int, input().split())
    #그래프를 저장하는 리스트
    table = [[] for _ in range(m+1)]
    #들어오는 간선의 갯수를 저장하는 배열
    insert = [0 for _ in range(m+1)]
    for j in range(p):
        s, e = map(int, input().split())
        insert[e] += 1
        table[s].append(e)
    
    print(i, topological_sort())