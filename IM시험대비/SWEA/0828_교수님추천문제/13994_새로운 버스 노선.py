import sys

sys.stdin = open('13994.txt')

'''
공통사항: A에서 출발해 B에 도착하므로 A와 B는 반드시 포함할 것

일반: A와 B 사이 모든 정류장에 정차
급행: A가 짝수 - A, B 사이의 모든 짝수에 정차함
      A가 홀수 - A, B 사이의 모든 홀수에 정차함
광역: A가 짝수 - A와 B 사이의 모든 4의 배수 번호 정류장에 정차
      A가 홀수 - A와 B 사이의 3의 배수이면서 10의 배수가 아닌 번호 정류장에 정차

최대 몇 개의 노선이 같은 정류장에 정차하는지 알아내보자
'''

T = int(input())
for tc in range(1, T + 1):
    buses = int(input())
    busStop = [0]
    for bus in range(buses):
        busType, A, B = map(int, input().split())

        if len(busStop) < B+1:
            busStop.extend([0] * (B - len(busStop) + 1))

        busStop[A] += 1
        busStop[B] += 1

        if busType == 1:
            for stop in range(A + 1, B):
                busStop[stop] += 1
        elif busType == 2:
            for stop in range(A + 2, B, 2):
                busStop[stop] += 1
        else:
            if A % 2:
                m = A % 3
                for stop in range(A + (3 - m), B, 3):
                    if stop % 10:
                        busStop[stop] += 1
                    else:
                        continue
            else:
                m = A % 4
                for stop in range(A + (4 - m), B, 4):
                    busStop[stop] += 1
    print(f'#{tc} {max(busStop)}')
