# coding: utf-8
# @Author : lryself
# @Date : 2022/10/10 0:13
# @Software: PyCharm
"""
题目：
输入：一个数n
输出一个螺旋正方形(外旋)

n=3
7 8 9
6 1 2
5 4 3

n=4
7 8 9 10
6 1 2 11
5 4 3 12
16 15 14 13
"""
from typing import List


def calSprialSquare(n: int) -> List[List[int]]:
    graph = [[0 for _ in range(n)] for _ in range(n)]
    # todo 赋值逻辑

    return graph


if __name__ == '__main__':
    n = 4
    g = calSprialSquare(n)
    for i in range(n):
        for j in range(n):
            print(g[i][j], end=" ")
        print()
