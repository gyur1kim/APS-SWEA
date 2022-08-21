import sys
sys.stdin = open('13755.txt')

def palindrome(arr, N, strLens):
    arrRotate = list(map(list, zip(*arr)))
    # 가로로 된 문장 찾기 -> 세로로 된것도 걍 돌림;;;힘드러
    for i in range(N):                     # 행
        for j in range(N - strLens + 1):   # 열
            output = ''
            for k in range(strLens):
                if arr[i][j+k] != arr[i][j+strLens-1-k]:
                    break
                output += arr[i][j+k]
            else:
                return output

            output = ''
            for k in range(strLens):
                if arrRotate[i][j + k] != arrRotate[i][j + strLens - 1 - k]:
                    break
                output += arrRotate[i][j + k]
            else:
                return output
            # 여기는 슬라이싱으로 푼 것
            # char1 = arr[i][j:j+strLens]
            # char2 = arrRotate[i][j:j+strLens]
            # if char1 == char1[::-1]:
            #     return ''.join(char1)
            # elif char2 == char2[::-1]:
            #     return ''.join(char2)


T = int(input())
for t in range(1, T+1):
    N, lenM = map(int, input().split())
    text = [list(input()) for _ in range(N)]

    ans = palindrome(text, N, lenM)
    print(f'#{t} {ans}')

