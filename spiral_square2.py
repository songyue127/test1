# coding: utf-8
# @Author : lryself
# @Date : 2022/10/10 0:13
# @Software: PyCharm
"""
题目：
输入：一个数n
旋输出一个螺三角形(内旋)

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
    level = 1
    direction = 3  # 0-左 1-下 2-上 3-右
    row = 0
    col = 0
    for a in range(1,n*(1+n)//2 + 1):
        graph[row][col] = a
        # for i in range(0,3):
        # for j in range(3,0,-1):
        # if row == n-level-j and col == n-level-i:
        if row == level - 1 and col == n - level:
            direction = 1
        elif row == n-level and col == level-1:
            direction = 2
        elif row == level and col == level - 1:
            direction = 3
            level +=1

        if direction == 1:
            row += 1
            col -= 1
        elif direction == 3:
            col += 1
        elif direction == 2:
            row -= 1

    return graph


if __name__ == '__main__':
    n = 4
    g = calSprialSquare(n)
    for i in range(n):
        for j in range(n):
            print(g[i][j], end=" ")
        print()
