import sys
sys.stdin = open('1210.txt')

for _ in range(10):
    t = int(input())
    ladderArr = [list(map(int, input().split())) for _ in range(100)]
    goX = 0
    goY = 99
    for i in range(100):
        if ladderArr[99][i] == 2:
            goX = i

    # while goY > 0:
    #     if goX-1 == -1:  # 맨 왼쪽에 있을 때
    #         if ladderArr[goY][goX+1] == 1:
    #             while goX+1 != 100 and ladderArr[goY][goX+1] == 1:
    #                 goX += 1
    #     elif goX+1 == 100:  # 맨 오른쪽
    #         if ladderArr[goY][goX-1] == 1:
    #             while goX-1 != -1 and ladderArr[goY][goX-1] == 1:
    #                 goX -= 1
    #     else:
    #         if ladderArr[goY][goX + 1] == 1 and goX-1 != -1:
    #             while goX + 1 != 100 and ladderArr[goY][goX + 1] == 1:
    #                 goX += 1
    #         elif ladderArr[goY][goX - 1] == 1:
    #             while goX - 1 != -1 and ladderArr[goY][goX - 1] == 1:
    #                 goX -= 1
    #     goY -= 1

    # 종현님이 줄여주셨다 뀻~~
    while goY > 0:
        if goX+1 != 100 and ladderArr[goY][goX + 1] == 1:
            while goX + 1 != 100 and ladderArr[goY][goX + 1] == 1:
                goX += 1
        elif goX-1 != -1 and ladderArr[goY][goX - 1] == 1:
            while goX - 1 != -1 and ladderArr[goY][goX - 1] == 1:
                goX -= 1
        goY -= 1
    print(f'#{t} {goX}')

