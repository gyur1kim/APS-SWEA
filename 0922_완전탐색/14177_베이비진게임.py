import sys
sys.stdin = open('14177.txt')


def babyGin(lst, card, now):
        lst[card] += 1
        if lst[card] == 3:
            return now

        cnt = 0
        for j in range(card - 2, card + 3):
            if j < 0 or j > 9:
                continue
            else:
                if lst[j]:
                    cnt += 1
                    if cnt == 3:
                        return now
                elif lst[j] == 0 and cnt != 0:
                    return 0
        return 0

T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))[::-1]
    player1 = [0]*10
    player2 = [0]*10

    res = ''
    for i in range(12, 0, -1):
        card = cards.pop()
        if i%2:
            res = babyGin(player2, card, '2')
        else:
            res = babyGin(player1, card, '1')
        if res:
            break
    print(f'#{tc} {res}')