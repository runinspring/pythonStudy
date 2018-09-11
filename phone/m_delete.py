# 从iphonex 的数据中删除坚果的数据
import pymysql
# 打开数据库连接
db = pymysql.connect("localhost", "test", "123456", "JD_PHONE")
cursor = db.cursor()

# sql = "SELECT * FROM cm_test WHERE locate('锤子',referenceName)" # 查询有锤子的字段
sql = "DELETE FROM cm_iphonex WHERE locate('锤子',referenceName)"  # 删除有锤子的字段

try:
    print('sql', sql)
    # 执行sql语句
    cursor.execute(sql)
    db.commit()
    # 获取所有记录列表
    # results = cursor.fetchall()
    # # print('results:', results)
    # for row in results:
    #     print('row', row)
    #     print('-----')
except Exception as e:
    print('rollback', e)
    # 如果发生错误则回滚
    db.rollback()

db.close()
