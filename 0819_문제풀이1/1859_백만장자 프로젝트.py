import sys
sys.stdin = open('1859.txt')

def billionaire(priceList):
    if len(priceList) < 2:
        return 0

    today = 0  # 오늘 날짜, 인덱스
    tomorrow = today + 1 # 이건 내일

    while priceList[today] > priceList[tomorrow]:  # 만약 오늘이 내일보다 비싸면 사지 마
        if tomorrow+1 < len(priceList):
            today += 1
            tomorrow += 1
        else:
            return 0

    buy = 0   # 드디어 내일이 더 비싸!! 산 가격을 담을 함수
    cnt = 0  # 구매 횟수
    highestPrice = priceList[tomorrow]  # 여지껏 가장 비쌌던 가격과 날짜를 저장
    highestDay = tomorrow
    highestDayBought = 0  # 가장 비쌌을 때 누적된 구매 가격...
    highestDayBoughtCnt = 0 # 가장 비쌌을 때는 몇 개 구매했었는지.....

    while (tomorrow < len(priceList)) or (buy < priceList[tomorrow]*cnt):
        buy += priceList[today]
        cnt += 1
        if highestPrice < priceList[tomorrow]:
            highestPrice = priceList[tomorrow]
            highestDay = tomorrow
            highestDayBought = buy
            highestDayBoughtCnt = cnt
        today += 1
        tomorrow += 1

    if highestDay+1 >= len(priceList):
        return (highestPrice*highestDayBoughtCnt)-highestDayBought

    # while문 탈출 -> 계속 사기만 하면 손해가 발생한다는 뜻!
    return billionaire(priceList[highestDay+1:]) + ((highestPrice*highestDayBoughtCnt)-highestDayBought)


T = int(input())
for tc in range(1, T+1):
    days = int(input())
    pricesLst = list(map(int, input().split()))

    print(f'#{tc} {billionaire(pricesLst)}')