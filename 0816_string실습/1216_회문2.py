import sys
sys.stdin = open('1216.txt')


def palindrome(arr, revArr):
    for length in range(100, 0, -1):  # 확인할 글자 수, 100, 99,,, 1글자까지
        for i in range(100):                   # 이게 행
            for j in range(100 - length + 1):  # 이건 열(정확히는 열의 시작점)
                for l in range(length//2):
                    if arr[i][j+l] != arr[i][j+length-1-l]:
                        break
                else:
                    return length

                for l in range(length//2):
                    if revArr[i][j + l] != revArr[i][j + length - 1 - l]:
                        break
                else:
                    return length

for _ in range(10):
    t = int(input())
    arr = [list(input()) for _ in range(100)]
    revArr = list(zip(*arr))
    print(f'#{t} {palindrome(arr, revArr)}')

