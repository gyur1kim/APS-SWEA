import sys
sys.stdin = open('5356.txt')

T = int(input())
for tc in range(1, T+1):
    chars = []
    for _ in range(5):
        char = list(input())
        chars.append(char)
    ans = ''
    while True:
        for i in range(len(chars)):
            ans += chars[i].pop(0)
        chars = list(filter(lambda x: x, chars))
        if len(chars) == 0:
            break
    print(f'#{tc} {ans}')