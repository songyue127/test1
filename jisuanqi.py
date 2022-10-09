# coding: utf-8
# @Author : lryself
# @Date : 2022/9/24 23:19
# @Software: PyCharm


# 计算器
# 实现4个函数，分别的作用是加减乘除

# 加
def add(a, b: int):
    if a+b>=2^31 :
        return False
    pass


# 减
def dev(a, b: int):
    if a-b<=-2^31 :
        return False
    pass


# 乘
def mut(a, b: int):
    pass


# 除
def div(a, b: int):
    if b==0:
        return  False
    if a/b == 0:
        print("输入错误")
    pass


if __name__ == '__main__':
    # 输入一个m{+-*/}n
    s = input("请输入一个计算表达式：")
    if '+' in s:
        m = eval(s.split("+")[0])         #split分割加号前后的字符串
        n = eval(s.split("+")[1])
        add(m, n)
    elif '-' in s:
        m = eval(s.split("-")[0])
        n = eval(s.split("-")[1])
        dev(m, n)
    elif '*' in s:
        m = eval(s.split("*")[0])
        n = eval(s.split("*")[1])
        mut(m, n)
    elif '/' in s:
        m = eval(s.split("/")[0])
        n = eval(s.split("/")[1])
        div(m, n)
    else:
        print("输入错误，操作符只能为+-*/")