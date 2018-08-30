# -*- coding: utf-8 -*-
# 根据单字的武器名，获取长的武器名
import re

#读取小说内容，去除换行
sanguo = open('sanguo.txt').read().replace('\n', '')
# 获取拿武器的姿势，转成数组
newWeapon = open('new_weapon.txt').read().replace('\n', '').split(',')
if '' in newWeapon:
    newWeapon.remove('')
tempPos2 = []

for wea in newWeapon:
    #武器前后各取6个字
    reg = re.compile('.{4}%s.{4}' %wea)
    tempPos = reg.findall(sanguo)
    print(wea,tempPos)
    # tempPos = [pos + x for x in tempPos]
    # # print(pos, tempPos)
    # #找到的词条里是否包含之前的武器列表里的武器，如果在就忽略
    # for pos2 in tempPos:
    #     isNew = True#是否是新的武器
    #     for weapon in allWeapon:
    #         if weapon in pos2:
    #             # print('same',weapon,pos2)
    #             isNew = False
    #             break
    #     if isNew:
    #         tempPos2.append(pos2)
        
# print(666,pos, tempPos2)
