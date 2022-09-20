import sys
sys.stdin = open('14141.txt')


T = int(input())
for tc in range(1, T+1):
    l, numHex = input().split()
    ans = ''
    for h in numHex:
        b = bin(int(h, 16))[2:].zfill(4)
        ans += str(b)
    print(f'#{tc} {ans}')