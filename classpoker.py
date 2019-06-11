# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 13:48:17 2019

@author: 王振宁
"""

import random
class poker:#扑克的一个类，下面使用的变量如果在两个实例方法里使用，要定义成实例属性。要不然会出现后面不能引用前面的变量。
    def __init__(self):
        self.a=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,
                19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,
                36,37,38,39,40,41,42,43,44,45,46,47,48]
    def xipai(self):#洗牌
        random.shuffle(self.a)
        n=random.randint(1,49)
        b=self.a[:n]
        c=self.a[n:]
        self.a=c+b
    def fapai(self):#发牌
        self.str1=self.a[:-4:3]
        self.str2=self.a[1:-4:3]
        self.str3=self.a[2:-4:3]
        self.str4=self.a[-4:]
    def qiangdizhu(self):#抢地主
        n=random.randint(1,3)
        self.dizhu=n#定义一个实例属性，赋给地主的序号
        if n==1:
            self.str1+=self.str4
        if n==2:
            self.str2+=self.str4
        if n==3:
            self.str3+=self.str4
    def mapai(self):#码牌
        self.str1.sort(reverse=True)
        self.str2.sort(reverse=True)
        self.str3.sort(reverse=True)
    def yingshe(self):#映射
        paizd=[(0,'方片4'),(1,'梅花4'),(2,'红桃4'),(3,'黑桃4'),
               (4,'方片5'),(5,'梅花5'),(6,'红桃5'),(7,'黑桃5'),
               (8,'方片6'),(9,'梅花6'),(10,'红桃6'),(11,'黑桃6'),
               (12,'方片7'),(13,'梅花7'),(14,'红桃7'),(15,'黑桃7'),
               (16,'方片8'),(17,'梅花8'),(18,'红桃8'),(19,'黑桃8'),
               (20,'方片9'),(21,'梅花9'),(22,'红桃9'),(23,'黑桃9'),
               (24,'方片10'),(25,'梅花10'),(26,'红桃10'),(27,'黑桃10'),
               (28,'方片J'),(29,'梅花J'),(30,'红桃J'),(31,'黑桃J'),
               (32,'方片Q'),(33,'梅花Q'),(34,'红桃Q'),(35,'黑桃Q'),
               (36,'方片K'),(37,'梅花K'),(38,'红桃K'),(39,'黑桃K'),
               (40,'方片A'),(41,'梅花A'),(42,'红桃A'),
               (43,'方片2'),(44,'梅花2'),(45,'红桃2'),
               (46,'方片3'),(47,'梅花3'),(48,'红桃3')]
        zdpai = dict(paizd)
        paistr1=''
        for i in range (len(self.str1)):
            paistr1+=zdpai[self.str1[i]]+' '
        paistr2=''
        for i in range (len(self.str2)):
            paistr2+=zdpai[self.str2[i]]+' '
        paistr3=''
        for i in range (len(self.str3)):
            paistr3+=zdpai[self.str3[i]]+' '
        self.user1=paistr1 #这里要把牌的序列赋给三个玩家的实例属性
        self.user2=paistr2
        self.user3=paistr3
user=poker()#使用这个类时，要挨个使用实例的方法
user.xipai()
user.fapai()
user.qiangdizhu()
user.mapai()
user.yingshe()
print ('庄家:',user.dizhu)
print ('user1:',user.user1)
print ('user2:',user.user2)
print ('user3:',user.user3)
 