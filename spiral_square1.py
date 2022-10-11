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
import math


def calSprialSquare(n: int) -> List[List[int]]:
    graph = [[0 for _ in range(n)] for _ in range(n)]
    # todo 赋值逻辑
    level = 1
    direction = 0  # 0-右，1-左，2-下，，3-上
    row = (n-1)//2
    col = (n-1)//2
    # for a in range(1,n * n+1):
    for a in range(n * n):
        graph[row][col] = a + 1
        if row == level and col == n - level:
            direction = 2
        elif row == n - level and col == n - level:
            direction = 1
        elif row == n - level and col == level-1:
            direction = 3
        elif row ==level-1  and col == level-1:
            direction = 3
        elif row== level-1 and col == n - level:
            col += 1
            level += 1

        if direction == 0:
            col += 1
        elif direction == 2:
            row += 1
        elif direction == 1:
            col += 1
        elif direction == 3:
            row += 1

    return graph


if __name__ == '__main__':
    n = 3
    g = calSprialSquare(n)
    for i in range(n):
        for j in range(n):
            print(g[i][j], end=" ")
        print()
