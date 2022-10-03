import sys
sys.stdin = open('1945.txt')

T = int(input())
divide = [2, 3, 5, 7, 11]
for tc in range(1, T+1):
    num = int(input())
    exponents = []
    for i in divide:
        exponent = 0
        # print(num%i)
        while num%i == 0:
            num, m = divmod(num, i)
            exponent += 1
        exponents.append(exponent)
    print(f'#{tc}', *exponents)


