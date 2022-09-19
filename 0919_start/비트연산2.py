def Bbit_print(i):
    output = ""
    for j in range(7, -1, -1):
        output += "1" if i&(1<<j) else "0"
    print(output, end=" ")


# 0x는 16진수를 나타낼때 사용한다
a = 0x10
x = 0x01020304
print("%d = " % a, end='')
Bbit_print(a)
print()
print("0%x = " % x, end="")
for i in range(4):
    # 0xff는 11111111 이다.
    Bbit_print((x >> i*8) & 0xff)