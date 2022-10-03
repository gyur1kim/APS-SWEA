import sys
sys.stdin = open('13630.txt')

T = int(input())
for t in range(1, T+1):
    cnt = int(input())
    canvas = [[0]*10 for _ in range(10)]
    purple = 0

    for _ in range(cnt):
        x1, y1, x2, y2, color = list(map(int, input().split()))
        for j in range(x1, x2+1):
            for i in range(y1, y2+1):
                if canvas[i][j] == 0:       # 아무것도 안칠해있으면 칠한다.
                    canvas[i][j] = color
                elif canvas[i][j] == 3:     # 이미 보라색으로 칠해져있으면 건너뜀
                    continue
                elif canvas[i][j] != color: # 이미 칠해져있는데 나랑 다른 색이면?
                    canvas[i][j] = 3
                    purple += 1

    for c in canvas:
        print(*c)

    print(f'#{t} {purple}')
    print()
