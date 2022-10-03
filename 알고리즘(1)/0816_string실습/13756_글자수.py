import sys
sys.stdin = open('13756.txt')

T = int(input())
for t in range(1, T + 1):
    str1 = input()
    str2 = input()

    # str1set = list(set(str1))
    # str1dict = {}
    # for c in str1set:
    #     str1dict.update({c:0})

    str1dict = {}
    for c in str1:
        str1dict.update({c: 0})
    print(str1dict)
    for c in str2:
        if c in str1dict:
            str1dict[c] += 1
    print(str1dict)
    print(f'#{t} {max(str1dict.values())}')
