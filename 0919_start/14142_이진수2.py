import sys
sys.stdin = open('14142.txt')

T = int(input())
for tc in range(1, T+1):
    n = float(input())
    output = ''
    for i in range(12):
        n *= 2
        if n >= 1:
            output += '1'
            n -= 1
        else:
            output += '0'
        if n == 0:
            print(f'#{tc} {output}')
            break
    else:
        print(f'#{tc} overflow')