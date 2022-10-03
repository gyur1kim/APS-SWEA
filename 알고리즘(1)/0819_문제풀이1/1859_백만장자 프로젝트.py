import sys
sys.stdin = open('1859.txt')

'''
이 문제는 어려워보이지만..... 사고의 전환을 하면 쉬운 문제였다. ㅠ
미래를 알고 있으니깐, 그냥 미래가격에서부터 점점 앞으로 오면 된다
'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))
    earned = 0
    highest = prices[-1]
    for i in range(N-2, -1, -1):    # 미래에서 앞으로 오기, (뒤에서 두번째부터)
        if prices[i] < highest:
            earned += (highest - prices[i])
        else:
            highest = prices[i]

    print(f'#{tc} {earned}')