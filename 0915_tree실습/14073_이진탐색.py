import sys
sys.stdin = open('14073.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc} {N//2+1}')