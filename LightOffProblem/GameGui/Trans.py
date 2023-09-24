import random
import pygame
from pygame.locals import QUIT,KEYDOWN
import sys
import time
#生成数组lis和目标数组lisT
global width,height
width = x = int(input("x"))
height = y = int(input("y"))
lis = [[random.randint(0,1) for i in range(x)] for j in range(y)]
lisT = [[0 for i in range(x)] for j in range(y)]
print("目标",lisT)
print("生成",lis)

def Prlis(lis):
    #打印数组lis
    for i in range(len(lis)):
        tmp=''
        for j in range(len(lis[i])):
            tmp+=str(lis[i][j])
        print(tmp)

def change(x1,y1,lis):
    #改变状态
        lis[y1][x1] = 1 - lis[y1][x1]
        if x1 > 0:
            lis[y1][x1-1] = 1 - lis[y1][x1-1]
        if x1 < width-1:
            lis[y1][x1+1] = 1 - lis[y1][x1+1]
        if y1 > 0:
            lis[y1-1][x1] = 1 - lis[y1-1][x1]
        if y1 < height-1:
            lis[y1+1][x1] = 1 - lis[y1+1][x1]

def check(x1,y1):
    #检查坐标正确度
    if x1 >= width or y1 >= height or x1<0 or y1<0:
        return False
    else:
        return True
    
def GuiTrans(lis):
    #将0,1转化为灯的亮灭并显示
    colors = [[0,0,0],[255,165,79]]
    global location,x0,y0
    location = [[],[]]
    x = len(lis[0])
    y = len(lis)
    x0 = (800 - (90*x-50))/2
    y0 = (800 - (90*y-50))/2
    for i in range(len(lis)):
        for j in range(len(lis[i])):
            x1 = x0+50*j
            y1 = y0+50*i
            if x1 not in location[0]:
                location[0].append(x1)
            if y1 not in location[1]:    
                location[1].append(y1)
            pygame.draw.circle(screen,colors[lis[i][j]],[x1,y1],20,0)
def find_pos(x,y):
    for i in location[0]:
        for j in location[1]:
            L1 = i-20
            L2 = i+20
            R1 = j-20
            R2 = j+20
            if L1<=x<=L2 and R1<=y<=R2:
                return i,j
    return x,y

def See():
    #鼠标坐标可视化
    x,y = pygame.mouse.get_pos()
    x,y = find_pos(x,y)
    pygame.draw.rect(screen,[0,229,238],[x-22,y-22,44,44],2,1)
def click_trans():
    #翻译点击并做出响应
    flag = False
    clicked = pygame.mouse.get_pressed()
    x1,y1 = pygame.mouse.get_pos()
    if clicked[0]:
        flag = True
        x1,y1 = find_pos(x1,y1)
        print(x1,y1)
        x2 = int((x1-x0)//50)
        y2 = int((y1-y0)//50)
        print(x2,y2)
        if check(x2,y2):
            change(x2,y2,lis)
            time.sleep(0.2)
        
    
#初始化pygame
pygame.init()
screen = pygame.display.set_mode((800,800))
screen_color = [255,255,255]
screen.fill(screen_color)
clock = pygame.time.Clock()
#主程序
while True:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            pygame.quit()
            sys.exit()
    if lis == lisT:
        print("成功")
        break
    screen.fill(screen_color)
    GuiTrans(lis)
    See()
    click_trans()
    pygame.display.update()
    clock.tick(60)

    