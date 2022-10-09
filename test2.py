#  给你两个数，m,n，计算这两个数的减法，不能使用python自带的-

import random


def compare(m: str, n: str) -> int:
    a = len(m) - len(n)
    if a > 0:
        return 1
    elif a == 0:
        for i in range(len(m)):
            b = int(m[i]) - int(n[i])
            if b < 0:
                return -1
            elif b > 0:
                return 1
        return 0
    elif a < 0:
        return -1


def sub(m: str, n: str) -> str:
    flag = compare(m,n)
    if flag == 0:
        return '0'
    elif flag < 0:
        m,n=n,m

    a = len(n) - len(m)
    r = ''
    if a < 0:
        n = abs(a) * '0' + n
    b = len(m)
    e = 0
    for i in range(b):
        c = int(m[b - i - 1]) - int(n[len(n) - i - 1]) - e
        if c < 0:
            e = 1
            c = c + 10
        else:
            e = 0
        r = str(c) + r

    if flag < 0:
        return '-'+ r
    else:
        return r



if __name__ == '__main__':
    a = "1"
    b = "16"
    # r = random.randint(13, 30)
    # for i in range(r):
    #     a += f"{random.randint(0, 10)}"
    # r = random.randint(13, 30)
    # for i in range(r):
    #     b += f"{random.randint(0, 10)}"
    result = sub(a, b)
    print(f"\na={a}\nb={b}\na-b={result}")
