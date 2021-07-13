import sys
input = sys.stdin.readline

N = int(input())
line = []

for i in range(N):
    x, y = map(int, input().split())
    line.append((x, y))

line.sort()

maxx, maxy = line[0]
result = maxy - maxx
for i in range(1, N):
    tmx, tmy = line[i]
    if maxy < tmy:
        if tmx > maxy:
            result -= tmx - maxy
            maxx = tmx

        result += tmy - maxy
        maxy = tmy 
        
print(result)