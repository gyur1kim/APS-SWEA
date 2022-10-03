import sys
sys.stdin = open('1225.txt')


def makePassword(password):
    while True:
        for i in range(1, 6):
            if password[0] - i <= 0:
                password.append(0)
                password.pop(0)
                return password
            else:
                password.append(password[0] - i)
                password.pop(0)

for _ in range(1, 11):
    tc = int(input())
    password = list(map(int, input().split()))

    print(f'#{tc}', *makePassword(password))