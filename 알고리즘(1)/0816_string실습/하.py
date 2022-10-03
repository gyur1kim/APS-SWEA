# import sys
# sys.stdin = open('1216.txt')

def pal(lst):
    res = 1
    for row in lst:
        for i in range(n - res + 1):  # 열(문자열의 시작점..)
            for l in range(n - i - 1, res-1, -1): # 문자열 길이
                for j in range((l + 1)//2):  # 문자열 길이만큼
                    if row[i + j] != row[i + l - j]:  # 끝 글자랑 첫글자 비교함
                        break
                else:   # 다 돌면 이 문자열은 회문이당
                    if l + 1 > res:
                        res = l + 1
                    break
    return res     # 글자수..회문길이

n = 100
for _ in range(10):
    T = int(input())
    lst = [input().rstrip() for _ in range(n)]
    rev = list(map(lambda x: ''.join(x), zip(*lst)))
    a, b = pal(lst), pal(rev)
    res = a if a >= b else b
    print(f'#{T} {res}')