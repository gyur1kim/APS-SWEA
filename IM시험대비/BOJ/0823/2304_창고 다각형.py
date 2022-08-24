import sys
sys.stdin = open('2304.txt')

N = int(input())
pillars = [list(map(int, input().split())) for _ in range(N)]
pillars = sorted(pillars, key=lambda x: x[0])   # 기둥을 위치별로 정렬하기

# 젤 높은 기둥과 인덱스 찾기
highestPillar = 0
highestPillarIdx = 0
for i in range(N):
    if pillars[i][1] > highestPillar:
        highestPillar = pillars[i][1]
        highestPillarIdx = i

area = 0
# 앞에서부터 보기, 처음 기둥부터 젤 높은 기둥-1 까지 봄
nowHeight = pillars[0][1]
left = pillars[0][0]
i = 1
while i < highestPillarIdx:
    if pillars[i][1] > nowHeight:                    # 새로운 기둥의 높이가 기존 것보다 높으면
        area += nowHeight * (pillars[i][0] - left)   # 밑변 * 높이
        left = pillars[i][0]                         # 그리고 기둥의 최고 높이 갱신, 그 때의 left값 갱신
        nowHeight = pillars[i][1]
    i += 1

area += (pillars[highestPillarIdx][0] - left) * nowHeight   # 최고 높이 전에서 끝나서 마지막에 한 번 더 계산해야됨

# 뒤에서부터 보기
nowHeight = pillars[N - 1][1]
right = pillars[N-1][0] + 1
i = N-1-1
while i > highestPillarIdx:
    if pillars[i][1] > nowHeight:
        area += nowHeight * (right - (pillars[i][0]+1))
        right = pillars[i][0] + 1
        nowHeight = pillars[i][1]
    i -= 1
area += (right - (pillars[highestPillarIdx][0]+1)) * nowHeight

area += highestPillar    # 제일 높은 기둥 기준 양옆으로 넓이를 계산한거라서... 제일 높은 기둥의 넓이도 더해줘야 함
print(area)