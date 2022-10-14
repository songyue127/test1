# coding: utf-8
# @Author : lryself
# @Date : 2022/9/30 22:27
# @Software: PyCharm
import random


def div(a: str, b: str) -> (str, str):
    if b == "0":
        return "除数不能为0！", ""
    n = len(b)
    divisor = int(b)
    result = ""
    while True:
        for index in range(n, len(a)+1):  #不理解
            dividend = int(a[:index])
            if dividend >= divisor:
                break
        else:
            if result != "":
                return result, a.lstrip("0") if a != 0 else "0"  #lstrip用来去除开头字符，strip去除头尾字符，rstrip用来去除结尾字符（三者都可以去除空白符）
            return "0", a.lstrip("0") if a != 0 else "0"
        quotient = dividend // divisor
        remainder = dividend % divisor
        result += str(quotient)
        if index < len(a):
            a = str(remainder) + a[index:]
        else:
            a = str(remainder)


if __name__ == '__main__':

    for i in range(10000):
        d1 = random.randint(2, 10000000000000000)
        d2 = random.randint(2, d1)
        temp = div(str(d1), str(d2))
        r1 = int(temp[0])
        r2 = int(temp[1])
        if d1 // d2 != r1 and d1 % d2 != r2:
            print(f"你做错了! {d1},{d2} {r1}, {r2}")
            break
    else:
        print("你做对了！")
