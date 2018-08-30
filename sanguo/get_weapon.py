# -*- coding: utf-8 -*-
# 获取武器的种类
import re

# 获取拿武器的姿势，转成数组
newPos = open('new_pos.txt').read().replace('\n', '').split(',')
if '' in newPos:
    newPos.remove('')

def findWeapon():
    #读取小说内容，去除换行
    # sanguo = open('sanguo.txt', encoding='uft-8').read().replace('\n', '')
    # sanguo = open('sanguo.txt', encoding='GB18030').read().replace('\n', '')
    sanguo = open('sanguo.txt').read().replace('\n', '')
    allWeapon = open('all_weapon.txt').read().replace('\n', '').split(',')
    if '' in allWeapon:
        allWeapon.remove('')#移除空的
    tempPos2 = []
    print('newPos',newPos)
    for pos in newPos:
        #取出拿武器姿势到到下一个逗号或句号
        reg = re.compile('%s(.*?)[，,。]' % pos)
        tempPos = reg.findall(sanguo)
        tempPos = [pos + x for x in tempPos]
        # print(pos, tempPos)
        #找到的词条里是否包含之前的武器列表里的武器，如果在就忽略
        for pos2 in tempPos:
            isNew = True#是否是新的武器
            for weapon in allWeapon:
                if weapon in pos2:
                    # print('same',weapon,pos2)
                    isNew = False
                    break
            if isNew:
                tempPos2.append(pos2)
            
    print(666,pos, tempPos2)


#如果有新的拿武器姿势，查找武器
if newPos != []:
    findWeapon()
else:
    print('没有新的拿武器姿势')
