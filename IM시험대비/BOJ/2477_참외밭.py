import sys
sys.stdin = open('2477.txt')

fruits = int(input())
grounds = [list(map(int, input().split())) for _ in range(6)]

'''
이 사각형을 반시계 방향으로 조사하므로,
긴거->긴거->짧은거(안꺾)->짧은거(꺾)->짧은거(꺾)->짧은거(안꺾) 의 순서를 가짐.
그래서 젤 긴거를 찾으면 된당
젤 긴거 기준으로!!! 양 옆 값 중 긴 값이 긴거임.
긴거*긴거 - 짧은거(꺾)*짧은거(꺾) = 밭넓이..가 나온다.
'''
# 가장 긴 변을 찾는 과정
longest = 0
longestIdx = 0
for i in range(6):
    if grounds[i][1] > longest:
        longest = grounds[i][1]
        longestIdx = i

# 가장 긴 거 기준으로 양 옆을 보는데, 더 긴 애가 긴 변임. 그걸 찾아야됨
longer1 = grounds[longestIdx - 1][1]         # 가장 긴 거 전에 것
longer2 = grounds[(longestIdx + 1) % 6][1]   # 가장 긴 거 다음 것

if longer1 > longer2:            # 가장 긴 것 전에거가 더 길다면, longer2는 짧은것(안꺾)이라는 뜻이다!
    short1 = longest - grounds[longestIdx-2][1]   # 짧은것(꺾)
    short2 = longer1 - longer2                    # 짧은것(꺾)
    area = longest * longer1 - short1 * short2
else:
    short1 = longest - grounds[(longestIdx + 2)%6][1]   # 짧은것(꺾)
    short2 = longer2 - longer1                          # 짧은것(꺾)
    area = longest * longer2 - short1 * short2

print(area * fruits)