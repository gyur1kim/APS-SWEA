import sys
sys.stdin = open('1979.txt')

T = int(input())
for tc in range(1, T+1):
    sizeN, wordLen = map(int, input().split())
    puzzleArr = [list(map(int, input().split())) for _ in range(sizeN)]

    check = 0
    for i in range(sizeN):
        rowLst = []
        colLst = []
        for j in range(sizeN):
            # 행을 뒤져보자
            if puzzleArr[i][j] == 1:
                rowLst.append(1)
            elif puzzleArr[i][j] == 0:
                if len(rowLst) == wordLen:
                    check += 1
                rowLst = []

            # 열을 뒤져보자
            if puzzleArr[j][i] == 1:
                colLst.append(1)
            elif puzzleArr[j][i] == 0:
                if len(colLst) == wordLen:
                    check += 1
                colLst = []
        else:
            if len(rowLst) == wordLen:
                check += 1
            if len(colLst) == wordLen:
                check += 1
    print(f'#{tc} {check}')
    # ㅜ