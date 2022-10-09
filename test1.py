# coding: utf-8
# @Author : lryself
# @Date : 2022/9/25 23:35
# @Software: PyCharm

# 给你两个数，m,n，计算这两个数的加法，不能使用python自带的+
import random


def add(m: str, n: str) -> str:
    a = len(m) - len(n)
    r = ''
    if a < 0:
        m, n = n, m
        n = (-a) * '0' + n
    b = len(m)
    e = 0
    for i in range(b):
        c = int(m[len(m) - i - 1]) + int(n[len(n) - i - 1]) + e
        if c > 10:
            e = 1
            c = c - 10
        else:
            e = 0
        r = str(c) + r
    return r


if __name__ == '__main__':
    a = ""
    b = ""
    r = random.randint(13, 30)
    for i in range(r):
        a += f"{random.randint(0, 10)}"
    r = random.randint(13, 30)
    for i in range(r):
        b += f"{random.randint(0, 10)}"
    result = add(a, b)
    print(f"\na={a}\nb={b}\na+b={result}")


    # coding: utf-8
    # @Author : lryself
    # @Date : 2022/9/25 23:35
    # @Software: PyCharm

    # 给你两个数，m,n，计算这两个数的加法，不能使用python自带的+

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
            if c > 10:
                up = 1
            else:
                up = 0
            r = str(c - 10) + r
        return r


    if __name__ == '__main__':
        a = ""
        b = ""
        r = random.randint(13, 30)
        for i in range(r):
            a += f"{random.randint(0, 10)}"
        r = random.randint(13, 30)
        for i in range(r):
            b += f"{random.randint(0, 10)}"
        result = add(a, b)
        print(f"\na={a}\nb={b}\na+b={result}")
