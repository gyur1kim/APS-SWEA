import sys
sys.stdin = open('1220.txt')

for tc in range(1, 11):
    tableSize = int(input())
    table = [list(map(int, input().split())) for _ in range(tableSize)]

    cnt = 0
    for col in range(tableSize):
        oneCol = []
        for row in range(tableSize):
            oneCol.append(table[row][col])
        filteredLst = list(filter(lambda x: x>0, oneCol))

        while filteredLst[0] == 2:
            filteredLst.pop(0)
        while filteredLst[-1] == 1:
            filteredLst.pop()

        for i in range(len(filteredLst)-1):
            if filteredLst[i] == 2 and filteredLst[i+1] == 1:
                cnt += 1
        cnt += 1

    print(f'#{tc} {cnt}')