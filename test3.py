# 两个数m,n， 其中-1000 <= m,n <= 1000，求两个数相乘的结果
import random


def is_nature(m: str, n: str) -> bool:
    if m[0] == '-' and n[0] == '-':
        return True
    elif m[0] != '-' and n[0] != '-':
        return True
    return False


def add(m: str, n: str) -> str:
    a = len(m) - len(n)
    r = ''
    if a < 0:
        m, n = n, m
    n = abs(a) * '0' + n
    length = len(m)
    up = 0
    for i in range(length):
        c = int(m[length - 1 - i]) + int(n[length - 1 - i]) + up
        if c >= 10:
            up = 1
            c -= 10
        else:
            up = 0
        r = str(c) + r
    return (str(up) + r).lstrip("0")


def mut(m: str, n: str) -> str:
    flag = is_nature(m, n)

    # if m[0] == "-":
    #     m = m[1:]
    m = m.lstrip("-")
    n = n.lstrip("-")
    r = "0"

    # for index1 in range(len(m)):
    #     i = m[index1]
    #     for index2 in range(len(n)):
    #         j = n[index2]

    for index1, i in enumerate(m):
        for index2, j in enumerate(n):
            temp = int(i) * int(j) * pow(10, (len(m) - 1 - index1) + (len(n) - 1 - index2))
            r = add(r, str(temp))
    if flag:
        return r
    return '-' + r


if __name__ == '__main__':
    # todo 调试代码
    # m = "-8306"
    # n = "1952"
    # print(mut(m, n))

    # todo 测试代码
    for i in range(100):
        m = random.randint(-10000, 10000)
        n = random.randint(-10000, 10000)
        if eval(mut(str(m), str(n))) != m * n:
            print(f"计算错误！错误值：m={m},n={n}")
            break
    else:
        print("你做对了！")