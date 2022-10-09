from typing import List
if __name__ == '__main__':
    n = eval(input('请输入列数:'))
    line = [1,1]
    for i in range(2,n):
        a = line[i-1]+line[i-2]
        line.append(a)
    print(line)
