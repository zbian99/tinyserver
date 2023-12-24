import mysql.connector

# MySQL数据库连接配置
config = {
    'user': 'root',
    'password': 'kriuta1031',
    'host': 'localhost',
    'database': 'DATE_DB',
    'raise_on_warnings': True
}

# 创建数据库连接
connection = mysql.connector.connect(**config)

try:
    # 创建游标对象
    cursor = connection.cursor()

    # 执行查询语句
    query = "SELECT * FROM info;"
    cursor.execute(query)

    # 获取查询结果
    result = cursor.fetchall()

    # 遍历结果并输出
    for row in result:
        print(row)

except mysql.connector.Error as err:
    print("Error:", err)

finally:
    # 关闭游标和连接
    if 'cursor' in locals():
        cursor.close()
    if connection.is_connected():
        connection.close()
