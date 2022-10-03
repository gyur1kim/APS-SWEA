def itoa(num):
    isPositive = True
    if num<0:
        isPositive = False
        num = -num

    if num==0:
        return '0'

    str = ''
    while num:
        num, m = divmod(num, 10)
        str = chr(m + ord('0')) + str

    if isPositive:
        return str
    else:
        return '-'+str


def atoi(chars):
    # i = len(chars) - 1
    nums = 0
    for c in chars:
        # nums += (ord(c) - 48) * (10 ** i)
        # i -= 1
        nums = nums*10 + (ord(c) - ord('0'))
    return nums


print(itoa(-35280))
print(type(itoa(-35280)))
print('----------')
print(atoi('35280'))
print(type(atoi('35280')))