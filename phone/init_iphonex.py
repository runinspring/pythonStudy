import pymysql
# 打开数据库连接
db = pymysql.connect("localhost", "test", "123456", "JD_PHONE")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute() 方法执行 SQL，如果表存在则删除 慎重执行
# cursor.execute("DROP TABLE IF EXISTS cm_iphonex")

# phone:'iphone' #该字段为我创建的
# id: 11881798320,
# guid: "76744880-1eb4-4bf4-8fe7-4868969a4ed6"
# content: "很好和你联系吧我不是给你发过",
# creationTime: "2018-09-06 17:13:28",
# referenceName: "Apple iPhone X (A1865) 64GB 深空灰色 移动联通电信4G手机",
# userImageUrl: "misc.360buyimg.com/user/myjd-2015/css/i/peisong.jpg",
# nickname: "大***葵",
# productColor: "银色",
# memery:"64GB"
# userLevelName: "PLUS会员",
# 使用预处理语句创建表
sql = """CREATE TABLE cm_iphonex (
         id BIGINT not null primary key,
         guid  CHAR(40),
         content  TEXT,
         creationTime  CHAR(30),
         referenceName CHAR(255),
         userImageUrl CHAR(255),
         nickname CHAR(20),
         memery CHAR(20),
         userLevelName CHAR(20) )"""

try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
    print('succ')
except Exception as e:
    print('rollback',e)
    # 如果发生错误则回滚
    db.rollback()

# 关闭数据库连接
db.close()
