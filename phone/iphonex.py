import pymysql
import requests
import re
import json


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


def getURL(page):
    url = 'https://sclub.jd.com/comment/productPageComments.action?&productId=5089253&score=0&sortType=6&page=%s&pageSize=10&isShadowSku=0&rid=0&fold=1' % page
    # url = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv80592&productId=5089253&score=0&sortType=5&page=%s&pageSize=10&isShadowSku=0&rid=0&fold=1' % page
    # json_start = 'fetchJSON_comment98vv80592\('  # json 要过滤的开头文件，这个字符串会变 记得 \( 前面要加转义符
    content = requests.get(url)
    # print(url)
    print(content.json()['comments'])
    # reg = re.compile('%s' % json_start)
    # data0 = reg.sub('', content)
    # # re.sub('%s' % json_start, '', content)
    # data1 = re.sub('\);', '', data0)
    # data = json.loads(data1)
    # print(data['comments'])


def testData():
    dic = {'a': 12, 'b': {'b1': 12}}
    print(getData(dic, 'a'))
    print(getData(dic, 'b', 'c'))
    print(getData(dic, 'b', 'b1'))
    # if 'c' in dic['b']:
    #     print('ues')
    # else:
    #     print('no')
    # if 'c' in dic['b']:
    #     print('ues')
    # else:
    #     print('no')
    # print(dic['a'],dic['b']['c'])
    # data1 = open('test.json').read()
    # datas = json.loads(data1)
    # for item in datas['comments']:
    #     print(item)
    # print('nickname',item['nickname'])
    # print(datas['comments'])


def setData():
    data1 = open('test.json').read()
    datas = json.loads(data1)
    values = []
    for item in datas['comments']:
        # values.append((getData(item, 'id'), getData(item, 'nickname')))
        values.append((getData(item, 'id'), getData(item, 'guid'),
                       getData(item, 'content'), getData(item, 'creationTime'),
                       getData(item, 'referenceName'),
                       getData(item, 'userImageUrl'), getData(
                           item, 'nickname'),
                       getData(item['productSales'][0], 'saleValue'),
                       getData(item, 'userLevelName')))

        # print(getData(item['productSales'][0], 'saleValue'))

    db = pymysql.connect("localhost", "test", "123456", "JD_PHONE")
    cursor = db.cursor()
    # print('values', values)
    # sql = "INSERT INTO cm_iphonex (id, nickname) VALUES (%s,%s)"
    # sql = "REPLACE INTO cm_iphonex (id, nickname) VALUES (%s,%s)"
    sql = "INSERT INTO cm_iphonex (id, guid,content,creationTime,referenceName,userImageUrl,nickname,memery,userLevelName) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) "
    sql += "ON DUPLICATE KEY UPDATE userLevelName=Values(userLevelName)"  # 重复的替换
    # sql = "REPLACE INTO cm_iphonex (id, guid,content,nickname) VALUES (%s,%s,%s,%s)"
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


# d1 = {'a': [{"b": 12}]}
# s = getData2(d1['a'][0], 'b')
# print(s)
# testData()
setData()
# getURL(0)
