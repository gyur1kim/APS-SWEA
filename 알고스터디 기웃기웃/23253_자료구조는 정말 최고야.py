import sys
sys.stdin = open('23253.txt')

def checkDummies(M):
    for _ in range(M):
        n = int(sys.stdin.readline())
        bookStack = list(map(int, sys.stdin.readline().split()))
        for i in range(n-1):
            if bookStack[i] < bookStack[i+1]:
                return 'No'
    else:
        return 'Yes'

booksN, dummiesM = map(int, sys.stdin.readline().split())
print(checkDummies(dummiesM))

