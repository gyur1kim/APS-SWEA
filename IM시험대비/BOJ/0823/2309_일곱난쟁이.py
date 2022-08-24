import sys
sys.stdin = open('2309.txt')


def findDwarfs(arr):
    for i in range(9):
        for j in range(i + 1, 9):
            if arr[i] + arr[j] == strangersSum:    # i, j값의 합이 가짜 난쟁이 키의 합을 구하면
                arr.pop(j)                         # j부터 뺀다
                arr.pop(i)                         # 뒤에부터 빼면 앞의 idx는 변하지 않지만, 앞의 값을 빼면 뒤에 idx가 변해서...
                return arr


dwarfs = sorted([int(input()) for _ in range(9)])   # 받을 때부터 정렬해버리기
strangersSum = sum(dwarfs) - 100                    # 다른 애들은 100이니까, 전체에서 100만큼 빼면 가짜 난쟁이의 키의 합이 나옴
print(*findDwarfs(dwarfs))                          # 함수에 넣자
