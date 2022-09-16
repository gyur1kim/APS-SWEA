import sys
sys.stdin = open('5688.txt')

import math
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    exp = round(N**(1/3), 2)
    print(f'#{tc} {int(exp) if math.floor(exp) == math.ceil(exp) else -1}')