# 两个数m,n， 其中-1000 <= m,n <= 1000，求两个数相除的结果

def compare(a:str,b:str) -> int:
    if a < 0 and b < 0:
        return True
    elif a > 0 and b > 0:
        return True
    return False

def div(a:str,b:str): ->str
    r = ''
    divisor = eval(b)
    while True:
        index = len(b)
        dividend = eval(a[:index])
        while dividend < divisor:
            index = index + 1
            if index > len(a):
                r = '0'
            elif len(r) != 0:
                r = a
        quotient = dividend // divisor
        remainder = dividend % divisor
        r = r + str(quotient)
        if len(a) <= divisor and eval(a) < divisor:
            break
    return r,remainder








# if __name__ == '__main__':
#
#     for i in range(10000):
#         d1 = random.randint(2, 10000000000000000)
#         d2 = random.randint(2, d1)
#         temp = div(str(d1), str(d2))
#         r1 = int(temp[0])
#         r2 = int(temp[1])
#         if d1 // d2 != r1 and d1 % d2 != r2:
#             print(f"你做错了! {d1},{d2} {r1}, {r2}")
#             break
#     else:
#         print("你做对了！")