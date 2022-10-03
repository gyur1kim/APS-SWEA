import sys
sys.stdin = open('13807.txt')

T = int(input())
for tc in range(1, T+1):
    words = input()
    brackets = []
    ans = 0
    for w in words:
        print(brackets)
        if w == '{' or w == '(':
            brackets.append(w)
        elif w == '}':
            if len(brackets) == 0 or brackets.pop() != '{':
                break
        elif w == ')':
            if len(brackets) == 0 or brackets.pop() != '(':
                break
    else:
        if len(brackets) == 0:
            ans = 1
    print(f'#{tc} {ans}')