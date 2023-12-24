import csv
import tool
from operator import itemgetter


def get_data_from_base():
    import mysql.connector
    data = {}
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

    # 写入数据到 CSV 文件

    try:
        # 创建游标对象
        cursor = connection.cursor()

        # 执行查询语句
        query = "SELECT * FROM info;"
        cursor.execute(query)

        # 获取查询结果
        result = cursor.fetchall()
        with open('data.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            # 遍历结果并输出
            for row in result:
                data[row[0]] = row
                print(row)
                writer.writerow(row)

        return data

    except mysql.connector.Error as err:
        print("Error:", err)

    finally:
        # 关闭游标和连接
        if 'cursor' in locals():
            cursor.close()
        if connection.is_connected():
            connection.close()


# 生成csv
# data = get_data_from_base()

def read_data_from_cvs():
    data = {}
    import csv

    # 打开CSV文件
    with open('data.csv', 'r', newline='') as file:
        # 创建一个CSV阅读器对象
        reader = csv.reader(file)

        # 遍历每一行数据
        for row in reader:
            # 在这里对每一行数据进行处理
            # 例如，打印每一行数据
            # print(row)
            data[row[0]] = row
    return data


data = read_data_from_cvs()

data_male = []
data_female = []

# 区分男女
for i in data:
    if data[i][3] == "男":
        data_male.append(data[i])
    else:
        data_female.append(data[i])

# 有效问卷份数
print(len(data_male), len(data_female))


def init_matrix(rhs, lhs):
    matrix = []
    for ri in rhs:
        temp = {"self_number": ri[0], "info": []}
        for li in lhs:
            elem = {"student_number": li[0],
                    "tot": 0,
                    "grade": tool.grade(ri[6], li[7]),
                    "cate": tool.cate(ri[8], li[9]),
                    "constellation": tool.constellation(ri[10], li[11]),
                    "hobby": tool.hobby(ri[12], li[12]),
                    "height": tool.height(ri[14], li[15]),
                    "bmi": tool.bmi(ri[14], ri[16], li[17]),
                    "home": tool.home(ri[18], li[19]),
                    "workplace": tool.workplace(ri[20], li[20])}
            # 权重相同
            for k in elem:
                if k != "tot" and k != "student_number":
                    elem["tot"] += elem[k]
            temp["info"].append(elem)
        temp["info"].sort(key=itemgetter("tot"), reverse=True)
        matrix.append(temp)
    return matrix


ma = init_matrix(data_male, data_female)
fe = init_matrix(data_female, data_male)

# for i in ma[0]["info"]:
#     print(i)



# matrix = ma
# for item in matrix:
#     print(item['self_number'])
#     order_items = []
#     string = ''
#     for index, person in enumerate(item['info']):
#         if index < 5:
#             order_items.append(person)
#     for i, v in enumerate(order_items):
#         if i < 4:
#             string += v['student_number']+','
#         else:
#             string += v['student_number']
#     print(string)


def update_database_order(matrix):
    import mysql.connector

    # 连接数据库
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="kriuta1031",
        database="DATE_DB"
    )

    # 创建游标对象
    cursor = conn.cursor()

    # 计算字符串
    for item in matrix:
        print(item['self_number'])
        order_items = []
        string = ''
        for index, person in enumerate(item['info']):
            if index < 5:
                order_items.append(person)
        for i, v in enumerate(order_items):
            if i < 4:
                string += v['student_number'] + ','
            else:
                string += v['student_number']
        print(string)

        # 定义要执行的更新语句
        student_id = item['self_number']
        sorted_string = string
        update_query = f"UPDATE info SET preference = '{sorted_string}' WHERE 学号 = '{student_id}';"

        # 执行更新语句
        cursor.execute(update_query)

    # 提交更改到数据库
    conn.commit()

    # 关闭游标和数据库连接
    cursor.close()
    conn.close()

    print("数据已成功更新。")

# update_database_order(ma)

update_database_order(fe)