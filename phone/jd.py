import requests
import re
import json


def getURL(page):
    url = 'https://sclub.jd.com/comment/productPageComments.action?&productId=5089253&score=0&sortType=6&page=%s&pageSize=10&isShadowSku=0&rid=0&fold=1'% page
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


getURL(0)
# print(type(response))
# print(response.text)
