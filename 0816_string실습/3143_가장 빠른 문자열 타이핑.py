import sys
sys.stdin = open('3143.txt')

T = int(input())
for t in range(1, T+1):
    strA, pattern = input().split()
    short = strA.replace(pattern, '_')
    print(short)
    print(f'#{t} {len(short)}')