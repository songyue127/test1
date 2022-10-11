# coding: utf-8
# @Author : lryself
# @Date : 2022/10/10 0:13
# @Software: PyCharm
"""
题目：
输入：一个数n
输出一个螺旋正方形(内旋)

n=3
1 2 3
8 9 4
7 6 5

n=5
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
"""
from typing import List


def calSprialSquare(n: int) -> List[List[int]]:
    graph = [[0 for _ in range(n)] for _ in range(n)]
    # todo 赋值逻辑
    a = 1
    left, right, up, down = 0, n - 1, 0, n - 1
    while left <= right and up <= down:
        for i in range(left, right + 1):
            graph[up][i] = a
            a = a + 1
        for j in range(up + 1, down + 1):
            graph[j][right] = a
            a = a + 1
        for i in range(right - 1, left - 1, -1):
            graph[down][i] = a
            a = a + 1
        for j in range(down - 1, up, -1):
            graph[j][left] = a
            a = a + 1
        left = left + 1
        right = right - 1
        up = up + 1
        down = down - 1

    return graph


def calSprialSquare1(n: int) -> List[List[int]]:
    graph = [[0 for _ in range(n)] for _ in range(n)]
    # todo 赋值逻辑
    level = 1
    direction = 0  # 0-右， 1-下， 2-左，3-上
    row = 0
    col = 0
    for a in range(n + 1):
        graph[row][col] = a
        if row == level - 1 and col == n - level:
            direction = 1
        elif row == n - level and col == n - level:
            direction = 2
        elif row == n - level and col == level - 1:
            direction = 3
        elif row == level and col == level - 1:
            direction = 0
            level += 1

        if direction == 0:
            col += 1
        elif direction == 1:
            row += 1
        elif direction == 2:
            col -= 1
        else:
            row -= 1

    return graph


if __name__ == '__main__':
    n = 4
    g = calSprialSquare(n)
    for i in range(n):
        for j in range(n):
            print(g[i][j], end=" ")
        print()
