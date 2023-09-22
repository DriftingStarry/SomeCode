# -*- coding: gbk -*-
import random 
'''
这是报废的垃圾函数，被一行代码代替了
def spawn(x,y):
    lis = []
    for i in range(y):
        lis.append([0]*x)
        for j in range(x):
            lis[i][j] = random.randint(0,1)
    return lis
'''
#生成数组lis
x = int(input("x"))
y = int(input("y"))
lis = [[random.randint(0,1) for i in range(x)] for j in range(y)]
lisT = [[0 for i in range(x)] for j in range(y)]
print("目标",lisT)
print("生成",lis)
#打印数组lis
def Prlis(lis):
    for i in range(len(lis)):
        tmp=''
        for j in range(len(lis[i])):
            tmp+=str(lis[i][j])
        print(tmp)
#改变状态
def change(x,y,lis):
    lis[x][y] = 1 - lis[x][y]
    if x == 0:
       lis[x+1][y] = 1 - lis[x+1][y]
    
        
        
#检查坐标正确度
def check(x1,y1,x,y):
    if x1 >= x or y1 >= y:
        return False
    else:
        return True
#主程序
while True:
    print("现在的数组为：")
    Prlis(lis)
    tmp = input("输入（坐标用,隔开。输入114514结束）：")
    if tmp == "114514":
        print("强制结束")
        break
    elif lis == lisT:
        print("成功")
        break
    else:
        tmp = tmp.split(",")
        x1 = int(tmp[0])
        y1 = int(tmp[1])
        if check(x1,y1,x,y):
            change(x1,y1,lis)
        else:
            print("输入有误！重新输入")

        



     