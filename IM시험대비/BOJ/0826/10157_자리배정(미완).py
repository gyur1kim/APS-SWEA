import sys
sys.stdin = open('10157.txt')


def checkAudience(w, h, k):
    if k > w*h:
        return 0
    num = 1
    i = 1   # 행이 움직움직
    j = 1
    while num <= k:
        pass

width, height = map(int, input().split())
audienceK = int(input())

'''
좌석번호가 x, y로 들어오는뎅...
x값이 행으로 들어가고 y값이 열로 들어가... 물론 idx+1임
그니까 x값이 width에 해당하고 y값이 height에 해당한다
'''

