import random
import itertools
import copy

rows = 3  # 行数
cols = 4  # 列数
# 生成数组lis和目标数组lisT
lis = [[random.randint(0,1) for i in range(cols)] for j in range(rows)]
lisT = [[0 for i in range(cols)] for j in range(rows)]
# print("目标", lisT)
# print("生成", lis)


def prlis(lis):
    # 打印数组lis
    for i in range(len(lis)):
        tmp = ''
        for j in range(len(lis[i])):
            tmp += str(lis[i][j]) + ' '
        print(tmp)


def flip(lis, x, y, rows, cols):
    lis[y][x] = 1 - lis[y][x]
    if y-1 >= 0:
        lis[y-1][x] = 1 - lis[y-1][x]
    if y+1 < rows:
        lis[y+1][x] = 1 - lis[y+1][x]
    if x-1 >= 0:
        lis[y][x-1] = 1 - lis[y][x-1]
    if x+1 < cols:
        lis[y][x+1] = 1 - lis[y][x+1]
    return lis


def flip_by_list(lis, fliplist, rows, cols):
    for y in range(len(fliplist)):
        for x in range(len(fliplist[y])):
            if fliplist[y][x] == 1:
               lis = flip(lis, x, y, rows, cols)
    return lis


def enum(rows, cols):
    # 生成所有可能的元素为0，1的列表
    lists = list(itertools.product([0, 1], repeat=cols))
    # 生成所有可能的二维列表
    matrices = list(itertools.product(lists, repeat=rows))
    return list(list(list(j) for j in i) for i in matrices)


def main(lis, rows, cols):
    for result in enum(rows, cols):
        temp = copy.deepcopy(lis)
        temp = flip_by_list(temp, result, rows, cols)
        if temp == lisT:
            return result


print("初始：")
prlis(lis)
out = main(lis, rows, cols)
print("结果：")
prlis(out)
