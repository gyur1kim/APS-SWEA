import sys
sys.stdin = open('13632.txt')

T = int(input())

for t in range(1, T+1):
    page, pA, pB = list(map(int, input().split()))

    startA = startB = 1
    endA = endB = page
    cntA = cntB = 0

    # while startA <= endA:
    #     cntA += 1
    #     midA = int((startA + endA)/2)
    #     if midA == pA:
    #         break
    #     elif midA < pA:
    #         startA = midA + 1
    #     else:
    #         endA = midA - 1
    #
    # while startB <= endB:
    #     cntB += 1
    #     midB = int((startB + endB)/2)
    #     if midB == pB:
    #         break
    #     elif midB < pB:
    #         startB = midB + 1
    #     else:
    #         endB = midB - 1
    #
    # if cntB > cntA:
    #     print(f'#{t} A')
    # elif cntB < cntA:
    #     print(f'#{t} B')
    # else:
    #     print(f'#{t} 0')

    while True:
        midA = int((startA + endA)/2)
        midB = int((startB + endB)/2)

        if midA == pA and midB == pB:
            print(f'#{t} 0')
            break
        if midA == pA:
            print(f'#{t} A')
            break
        if midB == pB:
            print(f'#{t} B')
            break

        if midA < pA:
            startA = midA
        elif midA > pA:
            endA = midA

        if midB < pB:
            startB = midB
        elif midB > pB:
            endB = midB

