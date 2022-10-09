from typing import List


def yh(n: int) -> List[List[int]]:  # n为层数
    # 对n==1做特殊处理
    if n == 1:
        return [[1]]
    # 1. 构造杨辉三角的初始两列
    lines = [[1], [1, 1]]
    # 2. i为行数，构建每一行的数组
    for i in range(2, n):
        new_line = [1]
        # 3. 构造new_line，index为当前构建元素的位置，范围是1到行数-1（因为第几行就会有几个元素，第一位和最后一位都为1）
        for index in range(1, i):
            # 4. 编写递推公式
            a = lines[i-1][index - 1] + lines[i-1][index]
            new_line.append(a)
        # 5. 给结尾添加1
        new_line.append(1)
        # 6. 将构建好的new_line加入lines
        lines.append(new_line)
    return lines


if __name__ == '__main__':
    n = 10
    for line in yh(n):
        for i in line:
            print(i, end=" ")
        print()