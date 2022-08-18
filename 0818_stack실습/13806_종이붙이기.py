import sys
sys.stdin = open('13806.txt')

def factorial(n):
    if n == 0:
        return 1
    if n < 3:
        return n
    return n * factorial(n-1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = 1
    side10 = N // 10

    for side20 in range(1, (N // 20) + 1):
        side10 -= 2
        cnt += int((factorial(side20+side10)/(factorial(side20)*factorial(side10)))*(2**side20))
    print(f'#{tc} {cnt}')