import sys
sys.stdin = open('1206.txt')

# 내 주변으로 5개를 볼거임, 살펴볼 range는 range(2, caseNum-2)
# 5개를 잘라서 볼까? 아무튼 기준 집이 5개중에 제일 크면 조망권 확보함. 2번째로 높은 집의 높이와 빼면 된다.
# 무한반복

for n in range(1, 11):
    caseNum = int(input())
    buildings = list(map(int, input().split()))

    res = 0
    for i in range(2, caseNum - 2):
        building = buildings[i-2:i+3]
        building.sort()
        if building[4] == buildings[i]:
            res += buildings[i] - building[3]
    print(f'#{n} {res}')
