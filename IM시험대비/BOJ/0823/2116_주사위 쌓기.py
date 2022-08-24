import sys
sys.stdin = open('2116.txt')


N = int(input())
dices = [list(map(int, input().split())) for _ in range(N)]

big = 6
nowIdx = dices[0].index(big)
addNum = 0
# for dice in dices[1:]:
