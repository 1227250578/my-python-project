# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 14:39:44 2019

@author: 王振宁
"""
import random
def chupai():
    str1=[];
    for i in range(0,15):
        str1.append(random.randint(1,49))
    zhj=1
    print(str1)
    if(zhj==1):
        xuanpai=input('请选择您要出的牌')
        paiall=[('方片4',0),('梅花4',1),('红桃4',2),('黑桃4',3),
                   ('方片5',4),('梅花5',5),('红桃5',6),('黑桃5',7),
                   ('方片6',8),('梅花6',9),('红桃6',10),('黑桃6',11),
                   ('方片7',12),('梅花7',13),('红桃7',14),('黑桃7',15),
                   ('方片8',16),('梅花8',17),('红桃8',18),('黑桃8',19),
                   ('方片9',20),('梅花9',21),('红桃9',22),('黑桃9',23),
                   ('方片10',24),('梅花10',25),('红桃10',26),('黑桃10',27),
                   ('方片J',28),('梅花J',29),('红桃J',30),('黑桃J',31),
                   ('方片Q',32),('梅花Q',33),('红桃Q',34),('黑桃Q',35),
                   ('方片K',36),('梅花K',37),('红桃K',38),('黑桃K',39),
                   ('方片A',40),('梅花A',41),('红桃A',42),
                   ('方片2',43),('梅花2',44),('红桃2',45),
                   ('方片3',46),('梅花3',47),('红桃3',48)]
        paiall = dict(paiall)
        print(paiall[xuanpai])
        if(xuanpai in paiall.keys()):
            if paiall[xuanpai] in str1:
                del str1[str1.index(paiall[xuanpai])]
                print(str1);
            else:
                print('牌未在手中')
        else:
            print('选择错误')
chupai()