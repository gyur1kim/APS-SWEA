import sys
sys.stdin = open('13627.txt')

T = int(input())
for t in range(1, T+1):
    maxDist, stops, chargeNum = map(int, input().split())
    charges = list(map(int, input().split()))  #충전소가 있는 곳
    cnt = 0
    accDist = 0

    if charges[0] <= maxDist:
        accDist += charges[0]  # 출발지에서 첫번째 충전소까지의 거리
    else:
        print(f'#{t} {cnt}')
        continue

    '''
    충전소에 왔어.
    내가 다음 충전소까지 가는 거리를 구해
    다음충전소까지 가도 아직 최대 거리보다 작아 -> 그러면 그냥 가는거야(i+=1)
    아니야 다음 충전소까지 못가 지금 충전해야돼 -> 그러면 지금 cnt를 하고 accDist를 초기화해 다시 가는거야
    '''

    for i in range(chargeNum-1):
        distBetween = charges[i+1] - charges[i]  # 다음 충전소까지의 거리

        if distBetween > maxDist:   # 다음 충전소가 못가는 거리면 끝낸다..
            print(f'#{t} 0')
            break

        if accDist + distBetween <= maxDist:  # 현재까지 온 거리에 다음 거리를 더해도 갈 수 있으면 가즈악~ 다음 충전소 가기
            accDist += distBetween
        else:   # 다음 충전소까지 못가면? 지금 충전하기(cnt += 1), 지금 위치에서 다음 위치까지 가자(accDist = distBetween)
            cnt += 1
            accDist = distBetween
    else:
        distBetween = stops - charges[-1]  # 마지막 정류소에서부터 도착지까지
        if distBetween > maxDist:  # 거리가 아예 안되면 0 리턴
            print(f'#{t} 0')
        elif accDist + distBetween <= maxDist:   # 지금까지 달려온거에 더 가도 되면 충전 안해도 되지? 지금까지 달린거 출력
            print(f'#{t} {cnt}')
        else:
            print(f'#{t} {cnt+1}')     #도착 전 마지막 충전소에서 충전하기(cnt+1)
