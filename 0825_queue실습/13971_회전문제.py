import sys
sys.stdin = open('13971.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    print(f'#{tc} {nums[M % N]}')