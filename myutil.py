4  # -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 21:55:58 2017

@author: XuGang
"""
import numpy as np
import ctypes


# 展示扑克函数
def card_show(cards, info, n):
    # 扑克牌记录类展示
    if n == 1:
        print(info)
        names = []
        for i in cards:
            names.append(i.name + i.color)
        print(names)
        # Moves展示
    elif n == 2:
        if len(cards) == 0:
            return 0
        print(info)
        moves = []
        for i in cards:
            names = []
            for j in i:
                names.append(j.name + j.color)
            moves.append(names)
        print(moves)
        # record展示
    elif n == 3:
        print(info)
        names = []
        for i in cards:
            tmp = []
            tmp.append(i[0])
            tmp_name = []
            # 处理要不起
            try:
                for j in i[1]:
                    tmp_name.append(j.name + j.color)
                tmp.append(tmp_name)
            except:
                tmp.append(i[1])
            names.append(tmp)
        print(names)


# 在Player的next_moves中选择出牌方法
def choose(next_move_types, next_moves, last_move_type, model, player_id):
    if model == "random":
        return choose_random(next_move_types, next_moves, last_move_type, player_id)


# random
def choose_random(next_move_types, next_moves, last_move_type, player_id):
    if (player_id == 1 or player_id == 2):
        # 要不起
        if len(next_moves) == 0:
            return "yaobuqi", []
        else:
            #            cho=input('选择')
            #            for tem in range(len(next_moves)):
            #                    if cho==str(next_moves[tem]):
            #                        return next_move_types[tem], next_moves[tem]
            # start不能不要
            if last_move_type == "start":
                r_max = len(next_moves)
            else:
                r_max = len(next_moves) + 1
            r = np.random.randint(0, r_max)
            # 添加不要
            if r == len(next_moves):
                return "buyao", []
        #        print(next_move_types[r], next_moves[r])
        return next_move_types[r], next_moves[r]

    else:
        for i in range(len(next_moves)):
            print(' ')
            for tem in next_moves[i]:
                print(tem.name + tem.color, end=',')
        endif = True
        if len(next_moves) == 0:
            return "yaobuqi", []
        while (endif):
            result = []
            select = input("选择您要出的牌")
            str = select.split(",")
            if select == "buyao" and last_move_type!='start':
                endif = False
                return "buyao", []
            elif len(select) > 2:
                for i in range(len(next_moves)):
                    for j in range(len(str)):
                        for tem in next_moves[i]:
                            if str[j] == tem.name + tem.color:
                                result.append(1)
                                #print('jiayi')
                    if len(result) == len(str):
                        endif = False
                        return next_move_types[i], next_moves[i]
                    else:
                        result = []
                        #print('选择错误1')
            elif len(select) == 2:
                for i in range(len(next_moves)):
                    for tem in next_moves[i]:
                        if select == tem.name + tem.color:
                            endif = False
                            return next_move_types[i], next_moves[i]
                        else:
                            print(' ')
            else:
                print('选择错误，系统将为你自动出牌')
                r_max = len(next_moves)
                r = np.random.randint(0, r_max)
                return next_move_types[r], next_moves[r]


#            start不能不要
#            if last_move_type == "start":

'''
            while True:
                 select = input("选择您要出的牌")
                 for i in range(len(next_moves)):
                     for tem in next_moves[i]:
                         if select == tem.name + tem.color:
                             return next_move_types[i], next_moves[i]
                         else :print("选择错误")
'''


# 发牌
def game_init(players, playrecords, cards,n):
    # 洗牌
    np.random.shuffle(cards.cards)
    # 排序
    p1_cards = cards.cards[:15]
    p1_cards.sort(key=lambda x: x.rank)
    p2_cards = cards.cards[15:30]
    p2_cards.sort(key=lambda x: x.rank)
    p3_cards = cards.cards[30:]
    p3_cards.sort(key=lambda x: x.rank)
    players[0].cards_left = playrecords.cards_left1 = p1_cards
    players[1].cards_left = playrecords.cards_left2 = p2_cards
    players[2].cards_left = playrecords.cards_left3 = p3_cards


    if n == 2:
        players[0].cards_left = playrecords.cards_left1 = p1_cards
        players[1].cards_left = playrecords.cards_left2 = p2_cards
        players[2].cards_left = playrecords.cards_left3 = p3_cards
    else:
        players[0].cards_left = playrecords.cards_left1 = p3_cards
        players[1].cards_left = playrecords.cards_left2 = p2_cards
        players[2].cards_left = playrecords.cards_left3 = p1_cards



