import sys
sys.stdin = open('13624.txt')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    cards = input()
    cardsList = [0]*10

    for n in cards:
        cardsList[int(n)] += 1    #i가 카드 숫자, v가 카드 갯수

    print(cardsList)
    numberOfCards = bigNum = -99
    for i, v in enumerate(cardsList):  #i가 카드에 적힌 숫자, v가 카드 갯수
        if v >= numberOfCards:
            numberOfCards = v
            bigNum = i

    print(f'#{t} {bigNum} {numberOfCards}')