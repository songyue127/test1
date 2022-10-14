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
    graph = [[0 for _ in range(n // 2 * 2 + 1)] for _ in range(n // 2 * 2 + 1)]       #2,3归一 成同一个矩阵
    # todo 赋值逻辑
    level = 0
    direction = 0  # 0-右，1-左，2-下，3-上
    base = n // 2
    row = base
    col = base
    for a in range(n * n):
        graph[row][col] = a
        graph[row][col] += 1
        if row == base - level and col == base + level:
            level += 1
        elif row == base - level + 1 and col == base + level:
            direction = 2
        elif row == base + level and col == base + level:
            direction = 1
        elif row == base + level and col == base - level:
            direction = 3
        elif row == base - level and col == base - level:
            direction = 0

        if direction == 0:
            col += 1
        elif direction == 2:
            row += 1
        elif direction == 1:
            col -= 1
        elif direction == 3:
            row -= 1

    return graph


if __name__ == '__main__':
    n = 7
    g = calSprialSquare(n)
    for i in range(n):
        for j in range(n):
            print(g[i][j], end=" ")
        print()
