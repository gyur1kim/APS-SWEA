import sys
sys.stdin = open('1210.txt')

for _ in range(10):
    t = int(input())
    ladderArr = [list(map(int, input().split())) for _ in range(100)]
    goY = 99

    # 종현님이 줄여주셨다 뀻~~
    # while goY > 0:
    #     if goX+1 != 100 and ladderArr[goY][goX + 1] == 1:
    #         while goX + 1 != 100 and ladderArr[goY][goX + 1] == 1:
    #             goX += 1
    #     elif goX-1 != -1 and ladderArr[goY][goX - 1] == 1:
    #         while goX - 1 != -1 and ladderArr[goY][goX - 1] == 1:
    #             goX -= 1
    #     goY -= 1

    # 유정 언니의 풀이법으로 풀어보기!
    XcanGo = []
    now = 0
    for i in range(100):
        if ladderArr[99][i] > 0:
            if ladderArr[99][i] == 2:
                now = len(XcanGo)
            XcanGo.append(i)
    # goX = XcanGo[index]

    while goY >= 0:
        if now < len(XcanGo)-1 and ladderArr[goY][XcanGo[now] + 1] == 1:
            now += 1
        elif now > 0 and ladderArr[goY][XcanGo[now] - 1] == 1:
            now -= 1
        goY -= 1
    print(f'#{t} {XcanGo[now]}')

