# 获取拿武器的动作
import re

# 获取武器的数据，转成数组
newWeapons = open('new_weapon.txt').read().replace('\n', '').split(',')
if '' in newWeapons:
    newWeapons.remove('')

def findPos():
    #读取小说内容，去除换行
    # sanguo = open('sanguo.txt', encoding='GB18030').read().replace('\n', '')
    sanguo = open('sanguo.txt').read().replace('\n', '')
    allPos = open('all_pos.txt').read().replace('\n', '').split(',')
    if '' in allPos:
        allPos.remove('')#移除空的
    tempPos2 = []
    print('newWeapons',newWeapons)
    for weapon in newWeapons:
        #取出武器前面的6个字
        reg = re.compile(r'(.{6}%s)' %weapon)
        tempPos = reg.findall(sanguo)
        # print('tempPos',tempPos,allPos)
        #找到的词条里是否包含之前的姿势列表里的姿势，如果在就忽略
        for pos2 in tempPos:
            isNew = True #是否是新的姿势
            for pos in allPos:
                if pos in pos2:
                    # print('use',pos2,pos,weapon)
                    isNew = False
                    break
            if isNew:
                tempPos2.append(pos2)

        
    print('weapon',tempPos2)
        # for pos in tempPos:
        #     if pos not in allPos:



#如果有新的武器，查找pos
if newWeapons != []:
    findPos()
else:
    print('没有新的武器')


