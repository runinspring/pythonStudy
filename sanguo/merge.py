# 合并 new 和 all，过滤相同的
import re

newPos = open('new_pos.txt').read().replace('\n', '').split(',')
allPos = open('all_pos.txt').read().replace('\n', '').split(',')
if '' in newPos:
    newPos.remove('')
if '' in allPos:
    allPos.remove('')
endPos = []

for pos in newPos:
    if pos not in endPos:
        endPos.append(pos)

for pos in allPos:
    if pos not in endPos:
        endPos.append(pos)

# 按照字数长短排序
endPos.sort(key=lambda x: len(x))
# 排序完了是短的到长的，翻转一下
endPos = endPos[::-1]
# print(111, endPos)

newWeapon = open('new_weapon.txt').read().replace('\n', '').split(',')
allWeapon = open('all_weapon.txt').read().replace('\n', '').split(',')
if '' in newWeapon:
    newWeapon.remove('')
if '' in allWeapon:
    allWeapon.remove('')
endWeapon = []

for weapon in newWeapon:
    if weapon not in endWeapon:
        endWeapon.append(weapon)

for weapon in allWeapon:
    if weapon not in endWeapon:
        endWeapon.append(weapon)

# 按照字数长短排序
endWeapon.sort(key=lambda x: len(x))
# 排序完了是短的到长的，翻转一下
endWeapon = endWeapon[::-1]

sanguo = open('sanguo.txt').read().replace('\n', '')

endPos2 = []
# 统计姿势出现的次数
for pos in endPos:
    reg = re.compile(r'(%s)' % pos)
    temp = reg.findall(sanguo)
    num = len(temp)
    endPos2.append({'name': pos, 'num': num})

# 统计武器出现的次数
endWeapon2 = []
for weapon in endWeapon:
    reg = re.compile(r'(%s)' % weapon)
    temp = reg.findall(sanguo)
    num = len(temp)
    endWeapon2.append({'name': weapon, 'num': num})

endPos2 = sorted(endPos2, key=lambda x: x['num'])
endPos2 = endPos2[::-1]

endWeapon2 = sorted(endWeapon2, key=lambda x: x['num'])
endWeapon2 = endWeapon2[::-1]

print(endPos2)

# fileAllWeapon = open('all_weapon.txt', 'w')
# fileAllWeapon.write()
# fileAllWeapon.close()
writeString = ('姿势一共%s种' % len(endPos2))
writeString += '\n\n'
writeString += ','.join(endPos)
writeString += '\n\n'
writeString += ('武器一共%s种' % len(endWeapon2))
writeString += '\n\n'
writeString += ','.join(endWeapon)
writeString += '\n\n'

for item in endPos2:
    writeString += item['name'] + ':' + str(item['num']) + '；'

writeString += '\n\n'
for item in endWeapon2:
    writeString += item['name'] + ':' + str(item['num']) + '；'


fileAllPos = open('result.txt', 'w')
fileAllPos.write(writeString)
fileAllPos.close()
