# coding: utf-8
# @Author : lryself
# @Date : 2022/10/10 0:13
# @Software: PyCharm
"""
题目：
输入：一个数n
输出一个螺旋三角形(内旋)

n=3
1 2 3
6 4
5

n=5
 1  2  3  4 5
12 13 14  6
11 15 7
10 8
9
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
