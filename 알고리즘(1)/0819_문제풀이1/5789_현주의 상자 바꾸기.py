import sys
sys.stdin = open('5789.txt')

T = int(input())
for tc in range(1, T+1):
    boxesN, timesQ = map(int, input().split())
    boxes = [0] * (boxesN)  # 주의 : 인덱스 -1 해서 들어감!
    for num in range(1, timesQ+1):
        start, end = map(int, input().split())
        for i in range(start-1, end):
            boxes[i] = num
    print(f'#{tc}', *boxes)