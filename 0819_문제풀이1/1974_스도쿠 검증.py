import sys
sys.stdin = open('1974.txt')


def checkSudoku(arr):
    # 가로 세로 체크
    for i in range(9):
        checkSudokuRow = set()
        checkSudokuCol = set()
        for j in range(9):
            if arr[i][j] not in checkSudokuRow:
                checkSudokuRow.add(arr[i][j])
            else:
                return 0
            if arr[j][i] not in checkSudokuCol:
                checkSudokuCol.add(arr[j][i])
            else:
                return 0

    # 3*3 체크
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            checkSudokuBox = set()
            for s1 in range(3):
                for s2 in range(3):
                    if arr[i+s1][j+s2] not in checkSudokuBox:
                        checkSudokuBox.add(arr[i+s1][j+s2])
                    else:
                        return 0
    return 1


T = int(input())
for tc in range(1, T+1):
    sudokuArr = [list(map(int, input().split())) for _ in range(9)]

    # 가로 세로 검증

    print(f'#{tc} {checkSudoku(sudokuArr)}')