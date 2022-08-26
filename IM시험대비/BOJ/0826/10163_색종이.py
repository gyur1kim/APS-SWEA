import sys
sys.stdin = open('10163.txt')

N = int(input())
painted = [0] * (N+1)
canvas = [[0]*1001 for _ in range(1001)]
for paper in range(1, N+1):
    x, y, w, h = map(int, input().split())

    for width in range(x, x+w):
        for height in range(y, y+h):
            if canvas[width][height] == 0:
                canvas[width][height] = paper
                painted[paper] += 1
            else:
                painted[canvas[width][height]] -= 1
                canvas[width][height] = paper
                painted[paper] += 1

for i in painted[1:]:
    print(i)