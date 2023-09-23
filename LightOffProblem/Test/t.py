import random
# 生成数组lis和目标数组lisT
lis = [[random.randint(0,1) for i in range(6)] for j in range(5)]
lisT = [[0 for i in range(6)] for j in range(5)]
print("目标", lisT)
print("生成", lis)


def prlis(lis):
    # 打印数组lis
    for i in range(len(lis)):
        tmp = ''
        for j in range(len(lis[i])):
            tmp += str(lis[i][j]) + ' '
        print(tmp)


prlis(lis)


def flip(lis, x, y):
    lis[y][x] = 1 - lis[y][x]
    if y-1 >= 0:
        lis[y-1][x] = 1 - lis[y-1][x]
    if y+1 < 5:
        lis[y+1][x] = 1 - lis[y+1][x]
    if x-1 >= 0:
        lis[y][x-1] = 1 - lis[y][x-1]
    if x+1 < 6:
        lis[y][x+1] = 1 - lis[y][x+1]
    prlis(lis)

