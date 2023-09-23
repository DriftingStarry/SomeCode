import pygame
import time
import sys
from pygame.locals import QUIT,KEYDOWN
import random
#初始化
pygame.init()
screen = pygame.display.set_mode((800,800))
screen_color = [255,255,255]
colorblack = [0,0,0]
coloryellow = [255,165,79]
colors = [colorblack,coloryellow]
def SpawnLight():
    for x in range(20,780,760//10):
        for y in range(20,780,760//10):
            pygame.draw.circle(screen,colors[random.randint(0,1)],[x,y],20.0,0)
#主函数
screen.fill(screen_color)
SpawnLight()
while True:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            pygame.quit()
            sys.exit()
    pygame.display.update()