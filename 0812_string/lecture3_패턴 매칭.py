# 브루트포스
text = 'this is a book'
pattern = 'is'

def bruteForce(text, patter):
    for i in range(len(text) - len(pattern) + 1):
        for j in range(len(pattern)):
            if text[i+j] != patter[j]:
                break
        else:
            return i
    return -1