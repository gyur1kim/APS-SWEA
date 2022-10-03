import sys
sys.stdin = open('13809.txt')

T = int(input())

for tc in range(1, T+1):
    words = list(input())
    i = 0

    while i < len(words)-1:
        if words[i] == words[i+1]:
            # words.remove(words[i])
            # words.remove(words[i])
            del words[i:i+2]
            if i-1 > -1:
                i -= 1
        else:
            i += 1
    print(f'#{tc} {len(words)}')