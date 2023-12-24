# import csv
#
# import csv
#
# # 打开 CSV 文件
# with open('./data/delete_student_number.csv', 'r', encoding="utf-8") as file:
#     # 创建 CSV 读取器
#     csv_reader = csv.reader(file)
#     line = 1
#     # 逐行遍历 CSV 文件
#     for row in csv_reader:
#         print(row)
#         line = line + 1
#     print(line)
#


import pandas as pd

# 读取 CSV 文件
file_path = './data/delete_student_number.csv'
df = pd.read_csv(file_path)

# 指定要删除的列
columns_to_drop = ['提交时间（自动）', '学员证/学生证照片（必填）', '请确认是否继续参加活动（必填）', '提交者（自动）']

# 删除指定列
df = df.drop(columns=columns_to_drop)

# 保存修改后的数据到新的 CSV 文件
output_file_path = './data/test1.csv'
df.to_csv(output_file_path, index=False)

print(f"Columns {columns_to_drop} deleted successfully.")


import pandas as pd
import mysql.connector
from mysql.connector import errorcode

# MySQL数据库连接配置
config = {
    'user': 'root',
    'password': 'kriuta1031',
    'host': 'localhost',
    'database': 'DATE_DB',
    'raise_on_warnings': True
}

# 本地CSV文件路径
csv_file_path = './data/test1.csv'

# 数据库表的名称
table_name = 'info'

try:
    # 连接到MySQL数据库
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    # # 创建数据库（如果不存在）
    # # cursor.execute(f"CREATE DATABASE IF NOT EXISTS {config['database']}")
    # connection.database = config['database']
    #
    # 创建表格（如果不存在）
#     create_table_query = """
#     CREATE TABLE IF NOT EXISTS {} (
#     学号 VARCHAR(255) PRIMARY KEY,
#     姓名 VARCHAR(255) NOT NULL CHARACTER SET utf8 COLLATE utf8_general_ci,
#     联系方式 VARCHAR(255) NOT NULL CHARACTER SET utf8 COLLATE utf8_general_ci,
#     本人性别 VARCHAR(255) NOT NULL CHARACTER SET utf8 COLLATE utf8_general_ci,
#     交友性别意向 VARCHAR(255) NOT NULL CHARACTER SET utf8 COLLATE utf8_general_ci,
#     年龄 VARCHAR(255) NOT NULL CHARACTER SET utf8 COLLATE utf8_general_ci,
#     你的年级 VARCHAR(255) NOT NULL CHARACTER SET utf8 COLLATE utf8_general_ci,
#     你希望TA的年级 VARCHAR(255) NOT NULL CHARACTER SET utf8 COLLATE utf8_general_ci,
#     身份类别 VARCHAR(255) NOT NULL CHARACTER SET utf8 COLLATE utf8_general_ci,
#     你希望对方是 VARCHAR(255) NOT NULL CHARACTER SET utf8 COLLATE utf8_general_ci,
#     你的星座 VARCHAR(255) NOT NULL CHARACTER SET utf8 COLLATE utf8_general_ci,
#     你希望TA的星座 VARCHAR(255) NOT NULL CHARACTER SET utf8 COLLATE utf8_general_ci,
#     你的兴趣爱好 VARCHAR(255) NOT NULL CHARACTER SET utf8 COLLATE utf8_general_ci,
#     自我介绍 VARCHAR(255) NOT NULL CHARACTER SET utf8 COLLATE utf8_general_ci,
#     你的身高 VARCHAR(255) NOT NULL CHARACTER SET utf8 COLLATE utf8_general_ci,
#     你希望TA的身高 VARCHAR(255) NOT NULL CHARACTER SET utf8 COLLATE utf8_general_ci,
#     你的体重 VARCHAR(255) NOT NULL CHARACTER SET utf8 COLLATE utf8_general_ci,
#     你希望TA的体型 VARCHAR(255) NOT NULL CHARACTER SET utf8 COLLATE utf8_general_ci,
#     你的家乡所在地 VARCHAR(255) NOT NULL CHARACTER SET utf8 COLLATE utf8_general_ci,
#     你希望TA家乡所在地 VARCHAR(255) NOT NULL CHARACTER SET utf8 COLLATE utf8_general_ci,
#     你希望未来在哪里发展 VARCHAR(255) NOT NULL CHARACTER SET utf8 COLLATE utf8_general_ci,
#     你希望和TA一起做的事 VARCHAR(255) NOT NULL CHARACTER SET utf8 COLLATE utf8_general_ci,
#     你的MBTI类型 VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci,
#     你的照片 VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci,
#     密码 VARCHAR(255) NOT NULL CHARACTER SET utf8 COLLATE utf8_general_ci
# );
#     # """.format(table_name)
    #
    # cursor.execute(create_table_query)
    #
    # # 读取CSV文件
    # df = pd.read_csv(csv_file_path)
    #
    # # 将数据写入数据库表
    # df.to_sql(name=table_name, con=connection, if_exists='replace', index=False)
    #
    import csv
    # 打开 CSV 文件
    with open('data/test1.csv', 'r', encoding="utf-8") as file:
        # 创建 CSV 读取器
        first = True
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if first:
                first = False
                continue
            print(row)
            cursor = connection.cursor()

            # 插入数据
            insert_query = f"""
                INSERT INTO {table_name} (学号, 姓名, 联系方式, 本人性别, 交友性别意向, 年龄, 你的年级, 你希望TA的年级, 身份类别, 你希望对方是, 你的星座, 你希望TA的星座, 你的兴趣爱好, 自我介绍, 你的身高, 你希望TA的身高, 你的体重, 你希望TA的体型, 你的家乡所在地, 你希望TA家乡所在地, 你希望未来在哪里发展, 你希望和TA一起做的事, 你的MBTI类型, 你的照片, 密码)
                VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s);
                """

            # 执行插入语句
            cursor.execute(insert_query, row)

            # 提交更改
            connection.commit()
            print(row)



    print("数据导入成功")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("用户名或密码错误")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("数据库不存在")
    else:
        print(err)

finally:
    # 关闭连接
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("数据库连接已关闭")
