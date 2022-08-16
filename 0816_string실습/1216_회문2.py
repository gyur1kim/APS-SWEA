import sys

sys.stdin = open('1216.txt')


def palindrome(arr, reversedArr):
    for i in range(100, 0, -1):  # 확인할 글자 수, 100, 99,,, 1글자까지
        for j in range(100):  # 이게 행
            for k in range(100 - i + 1):  # 이건 열....
                arr1 = []
                arr2 = []

                if arr[j][k] == arr[j][k+i-1]:
                    for l in range(k, k + i):
                        arr1.append(arr[j][l])
                    if arr1 == list(reversed(arr1)):
                        print(arr1)
                        return i
                if reversedArr[j][k] == reversedArr[j][k+i-1]:
                    for l in range(k, k + i):
                        arr2.append(reversedArr[j][l])
                    if arr2 == list(reversed(arr2)):
                        print(arr2)
                        return i

def palindrome2(arr, reversedArr):
    for i in range(100, 0, -1):            # 확인할 글자 수, 100, 99,,, 1글자까지
        for j in range(100):                # 이게 행
            for k in range(100 - i + 1):  # 이건 열....
                arr1 = []
                arr2 = []
                for l in range(k, k + i):
                    arr1.append(arr[j][l])
                    arr2.append(reversedArr[j][l])
                # if arr1 == list(reversed(arr1)) or arr2 == list(reversed(arr2)):
                #     print(f'{arr1 == list(reversed(arr1)) or arr2 == list(reversed(arr2))}')
                #     return i
                if arr1 == list(reversed(arr1)):
                    print(arr1)
                    return i
                elif arr2 == list(reversed(arr2)):
                    print(arr2)
                    return i



for _ in range(10):
    t = int(input())
    arr = [list(input()) for _ in range(100)]
    reversedArr = list(zip(*arr))
    print(f'#{t} {palindrome(arr, reversedArr)}')
    print(f'#{t} {palindrome2(arr, reversedArr)}')
