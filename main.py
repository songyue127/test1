def prime(x: int):
    if x < 2:
        return False
    if x == 2:
        return True
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


if __name__ == '__main__':       #测试函数是否正确
    for i in range(101):
        a = prime(i)
        if a:
            print(i, end=" ")    #让所有数据在一行
#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1
# def yanghui(n: int) -> None:
#     pass
# [[1],[1,3,1],[1,4,4,1],[1,5,8,5,1]]