# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 13:54:21 2019

@author: 王振宁
"""
background_image_filename = 'zhuomian.jpg'
mouse_image_filename = 'shubiao.jpg'

import sys
import pygame
pygame.init()

size = width, height = 600, 400

screen = pygame.display.set_mode(size)

background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
            sys.exit();
    screen.blit(background, (0,0))
    #将背景图画上去
    x, y = pygame.mouse.get_pos()
    #获得鼠标位置
    x-= mouse_cursor.get_width() / 2
    y-= mouse_cursor.get_height() / 2
    #计算光标的左上角位置
    screen.blit(mouse_cursor, (x, y))
    #把光标画上去
 
    pygame.display.update()
    #刷新一下画面