import sys
sys.stdin = open('2628.txt')


width, height = map(int, input().split())
cutCnt = int(input())
widthLst = [0, width]
heightLst = [0, height]

for cut in range(cutCnt):
    '''
    0: 가로로 자른다
    1: 세로로 자른다
    '''
    direction, num = map(int, input().split())

    if direction == 0:             # 가로로 자른다 -> height가 잘린다
        heightLst.append(num)
    else:                          # 세로로 자른다 -> width가 잘린다
        widthLst.append(num)

heightLst.sort()
widthLst.sort()
maxH = maxW = 0
for i in range(len(heightLst)-1):
    v = heightLst[i+1] - heightLst[i]
    maxH = max(maxH, v)
for i in range(len(widthLst)-1):
    v = widthLst[i+1] - widthLst[i]
    maxW = max(maxW, v)
print(maxH*maxW)