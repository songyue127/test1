# coding: utf-8
# @Author : lryself
# @Date : 2022/10/10 0:13
# @Software: PyCharm
"""
题目：
输入：一个数n
输出一个螺旋正方形

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
    left,right,up,down = 0,n-1,0,n-1
    while left<right and up<down:
        for i in range(left,right):
            a = graph[up][i]
            a = a+1
        for j in range(up,down):
            a = graph[j][right]
            a = a+1
        for i in range(right,left-1):
            a = graph[down][i]
            a = a+1
        for j in range(down,up-1):
            a = graph[j][left]
            a = a+1
        left = left-1
        right = right+1
        up = up-1
        down = down+1
        break

    return graph


if __name__ == '__main__':
    n = 3
    g = calSprialSquare(n)
    for i in range(n):
        for j in range(n):
            print(g[i][j], end=" ")
        print()

