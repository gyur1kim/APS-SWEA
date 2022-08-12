import sys
sys.stdin = open('13755.txt')

def palindrome(arr, N, strLens):
    arrRotate = list(map(list, zip(*arr)))
    # 가로로 된 문장 찾기 -> 세로로 된것도 걍 돌림;;;힘드러
    for i in range(N):
        for j in range(N - strLens + 1):
            char1 = arr[i][j:j+strLens]
            char2 = arrRotate[i][j:j+strLens]
            if char1 == char1[::-1]:
                return ''.join(char1)
            elif char2 == char2[::-1]:
                return ''.join(char2)


T = int(input())
for t in range(1, T+1):
    N, lenM = map(int, input().split())
    text = [list(input()) for _ in range(N)]
    # print(text)
    # print(text[0][0:0+lenM])
    # break
    ans = palindrome(text, N, lenM)
    print(f'#{t} {ans}')

