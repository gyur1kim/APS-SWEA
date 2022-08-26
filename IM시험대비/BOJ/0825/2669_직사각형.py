import sys
sys.stdin = open('2669.txt')

canvas = [[0]*100 for _ in range(100)]
cnt = 0
for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            if canvas[x][y] == 1:
                continue
            canvas[x][y] = 1
            cnt += 1

print(cnt)