import mysql.connector

def add_column(connection, column_name, column_type):
    try:
        # 创建游标对象
        cursor = connection.cursor()

        # 检查列是否存在
        query = f"SHOW COLUMNS FROM info LIKE '{column_name}';"
        cursor.execute(query)

        if not cursor.fetchone():
            # 如果列不存在，添加列
            alter_query = f"ALTER TABLE info ADD COLUMN {column_name} {column_type};"
            cursor.execute(alter_query)
            print(f"Column '{column_name}' added successfully.")

    except mysql.connector.Error as err:
        print("Error:", err)

    finally:
        # 关闭游标
        if 'cursor' in locals():
            cursor.close()

def insert_preference(connection, student_id, preference_value):
    try:
        # 创建游标对象
        cursor = connection.cursor()

        # 检查学号是否存在
        check_query = f"SELECT * FROM info WHERE 学号 = '{student_id}';"
        cursor.execute(check_query)

        if cursor.fetchone():
            # 如果学号存在，插入数据
            update_query = f"UPDATE info SET preference = '{preference_value}' WHERE 学号 = '{student_id}';"
            cursor.execute(update_query)
            connection.commit()
            print(f"Preference for 学号 '{student_id}' inserted successfully.")
        else:
            print(f"Error: 学号 '{student_id}' not found.")

    except mysql.connector.Error as err:
        print("Error:", err)

    finally:
        # 关闭游标
        if 'cursor' in locals():
            cursor.close()

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

# 调用增加列的函数
# add_column(connection, 'preference', 'VARCHAR(255)')

# 调用插入数据的函数
insert_preference(connection, '23026233', '23026233,23026233,23026233,23026233,23026167')

# 关闭数据库连接
if connection.is_connected():
    connection.close()
