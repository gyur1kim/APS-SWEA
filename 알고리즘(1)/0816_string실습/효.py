import sys
sys.stdin = open('1216.txt')

for case in range(1, 11):
    case_num = int(input())
    lst = [list((input())) for _ in range(100)]
    max_pan = 0

    for i in range(100):
        for j in range(100):
            # 가능한 회문 글자수 범위
            for k in range(1, 100 - j + 1):
                word = ''
                rv_word = ''
                # 회문의 길이
                for l in range(k):
                    word += lst[i][j + l]
                    rv_word += lst[i][j + k - 1 - l]
                if word == rv_word:
                    if len(word) > max_pan:
                        max_pan = len(word)

    for j in range(100):
        for i in range(100):
            # 가능한 회문 글자수 범위
            for k in range(1, 100 - i + 1):
                word = ''
                rv_word = ''
                # 회문의 길이
                for l in range(k):
                    word += lst[i + l][j]
                    rv_word += lst[i + k - 1 - l][j]
                if word == rv_word:
                    if len(word) > max_pan:
                        max_pan = len(word)

    print(f'#{case} {max_pan}')