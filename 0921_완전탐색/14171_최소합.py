import sys
sys.stdin = open('14171.txt')

# 완전 탐색으로 풀었다.... 수행시간과 메모리가 터지려한다 ㅋㅋ
def search(i, j, tmpMin):
    tmpMin += arr[i][j]
    if i == N-1 and j == N-1:
        global minV
        minV = min(minV, tmpMin) if minV else tmpMin
        return

    if i<N-1:
        search(i+1, j, tmpMin)
    if j<N-1:
        search(i, j+1, tmpMin)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minV = 0
    search(0, 0, 0)
    print(f'#{tc} {minV}')