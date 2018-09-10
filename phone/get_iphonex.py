import pymysql
import requests
import re
import json
import time


def getData(dic, key1, key2=None):
    if key1 in dic:
        if key2 is None:
            return dic[key1]
        elif key2 in dic[key1]:
            return dic[key1][key2]
        else:
            return None
    else:
        return None


def setData(datas):
    values = []
    for item in datas:
        values.append((getData(item, 'id'), getData(item, 'guid'),
                       getData(item, 'content'), getData(item, 'creationTime'),
                       getData(item, 'referenceName'),
                       getData(item, 'userImageUrl'), getData(
                           item, 'nickname'),
                       getData(item['productSales'][0], 'saleValue'),
                       getData(item, 'userLevelName')))

    db = pymysql.connect("localhost", "test", "123456", "JD_PHONE")
    cursor = db.cursor()
    sql = "INSERT INTO cm_iphonex (id, guid,content,creationTime,referenceName,userImageUrl,nickname,memery,userLevelName) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) "
    sql += "ON DUPLICATE KEY UPDATE userLevelName=Values(userLevelName)"  # 重复的替换
    try:
        # 执行sql语句
        cursor.executemany(sql, values)
        # 提交到数据库执行
        db.commit()
        print('succ')
    except Exception as e:
        print('rollback', e)
        # 如果发生错误则回滚
        db.rollback()
    # 关闭游标
    cursor.close()
    # 关闭数据库连接
    db.close()
    time.sleep(0.1)
    getURL()


idx = -1


def getURL():
    global idx
    
    if idx > 1:
        return
    print('url page:', idx)
    url = 'https://sclub.jd.com/comment/productPageComments.action?&productId=5089253&score=0&sortType=6&page=%s&pageSize=10&isShadowSku=0&rid=0&fold=1' % idx
    # url = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv80592&productId=5089253&score=0&sortType=5&page=%s&pageSize=10&isShadowSku=0&rid=0&fold=1' % page
    # json_start = 'fetchJSON_comment98vv80592\('  # json 要过滤的开头文件，这个字符串会变 记得 \( 前面要加转义符
    content = requests.get(url)
    # print(content.json())
    # print(len(content.json()['comments']))
    # print('----------')
    # reg = re.compile('%s' % json_start)
    # data0 = reg.sub('', content)
    # # re.sub('%s' % json_start, '', content)
    # data1 = re.sub('\);', '', data0)
    # data = json.loads(data1)
    # print(data['comments'])
    idx += 1
    setData(content.json()['comments'])


getURL()
# for i in range(0, 1000):
#     getURL(i)
#     time.sleep(0.1)

# d1 = {'a': [{"b": 12}]}
# s = getData2(d1['a'][0], 'b')
# print(s)
# testData()
# data1 = open('test.json').read()
# data2 = json.loads(data1)
# setData(data2['comments'])
# getURL(0)

# for i in range(0,10):
# print(i)
# time.sleep(1)

# tic1 = time.time()
# time.sleep(0.1)
# tic2 = time.time()
# print(tic2-tic1)
