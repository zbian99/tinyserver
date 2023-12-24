import mysql.connector
from flask import Flask, render_template, request, json

app = Flask(__name__)

config = {
    'user': 'root',
    'password': 'kriuta1031',
    'host': 'localhost',
    'database': 'DATE_DB',
    'raise_on_warnings': True
}

# 创建数据库连接
connection = mysql.connector.connect(**config)

student_info = ''


def validate_number(connection, student_id):
    try:
        # 创建游标对象
        cursor = connection.cursor()

        # 执行查询语句检查学号是否存在
        query = f"SELECT preference FROM info WHERE 学号 = '{student_id}';"
        cursor.execute(query)

        # 获取查询结果
        result = cursor.fetchone()

        # 如果结果不为空，返回 preference 值；否则，返回 None
        return result[0] if result else False

    except mysql.connector.Error as err:
        print("Error:", err)
        return False

    finally:
        # 关闭游标
        if 'cursor' in locals():
            cursor.close()


def get_order_student_number(student_id):
    try:
        # 创建游标对象
        cursor = connection.cursor()

        # 执行查询语句检查学号是否存在
        query = f"SELECT preference FROM info WHERE 学号 = '{student_id}';"
        cursor.execute(query)

        # 获取查询结果
        result = cursor.fetchone()

        # 如果结果不为空，返回 preference 值；否则，返回 None
        return result[0] if result else False

    except mysql.connector.Error as err:
        print("Error:", err)
        return False

    finally:
        # 关闭游标
        if 'cursor' in locals():
            cursor.close()


def get_person_info_by_student_number(student_number):
    try:
        # 创建游标对象
        cursor = connection.cursor()

        # 执行查询语句检查学号是否存在
        query = f"SELECT 年龄, 你的年级, 身份类别, 你的身高, 你的体重, 你的家乡所在地, 你希望未来在哪里发展, 你的星座, 你的兴趣爱好, 自我介绍, 你的照片 FROM info WHERE 学号 = '{student_number}';"
        cursor.execute(query)

        # 获取查询结果
        result = cursor.fetchone()

        # 如果结果不为空，返回姓名和联系方式；否则，返回 None
        return result if result else None

    except mysql.connector.Error as err:
        print("Error:", err)
        return None

    finally:
        # 关闭游标
        if 'cursor' in locals():
            cursor.close()


def get_name_and_contact_by_student_id(connection, student_id):
    try:
        # 创建游标对象
        cursor = connection.cursor()

        # 执行查询语句检查学号是否存在
        query = f"SELECT 姓名, 联系方式 FROM info WHERE 学号 = '{student_id}';"
        cursor.execute(query)

        # 获取查询结果
        result = cursor.fetchone()

        # 如果结果不为空，返回姓名和联系方式；否则，返回 None
        return result if result else None

    except mysql.connector.Error as err:
        print("Error:", err)
        return None

    finally:
        # 关闭游标
        if 'cursor' in locals():
            cursor.close()


def custom_sort(input_list, order):
    print(input_list, order)
    new = []
    for i in order:
        new.append(input_list[int(i) - 1])
    print(new)
    return new

    # return sorted(input_list, key=lambda x: order.index(order.index(x) + 1))


def update_data_by_student_id(connection, student_id, new_order):
    try:
        # 创建游标对象
        cursor = connection.cursor()

        # 执行查询语句检查学号是否存在
        query = f"SELECT preference FROM info WHERE 学号 = '{student_id}';"
        cursor.execute(query)

        # 获取查询结果
        result = cursor.fetchone()

        if result:
            # 如果学号存在，更新另一列的值
            result = result[0].split(',')
            sorted_list = custom_sort(result, new_order)
            sorted_string = ""

            for i, v in enumerate(sorted_list):
                print(i, v)
                if i == 4:
                    sorted_string = sorted_string + v
                else:
                    sorted_string = sorted_string + (v + ',')

            update_query = f"UPDATE info SET preference = '{sorted_string}' WHERE 学号 = '{student_id}';"
            cursor.execute(update_query)
            connection.commit()
            print(f"学号 '{student_id}' 对应的另一列值已更新为: {sorted_string}")
        else:
            print(f"学号 '{student_id}' 不存在。无法更新另一列的值。")

    except mysql.connector.Error as err:
        print("Error:", err)

    finally:
        # 关闭游标
        if 'cursor' in locals():
            cursor.close()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        number = request.form['number']
        # password = request.form['password']
        global student_info
        student_info = number
        # val = validate_number(connection, number, password)
        # val = validate_number(connection, number)
        val = get_order_student_number(number)
        if val:
            print(val)
            message = val.split(',')
            # message = ["同学" + str(i) + "信息    排序：" for i in range(5)]
            result = []
            for student_id in message:
                person = get_person_info_by_student_number(student_id)
                print(person)
                result.append(person)

            return render_template('dynamic.html',
                                   age1=result[0][0],
                                   grade1=result[0][1],
                                   cate1=result[0][2],
                                   height1=result[0][3],
                                   weight1=result[0][4],
                                   home1=result[0][5],
                                   workplace1=result[0][6],
                                   constellation1=result[0][7],
                                   hobby1=result[0][8],
                                   intro1=result[0][9],
                                   photo_data1=result[0][10],
                                   age2=result[1][0],
                                   grade2=result[1][1],
                                   cate2=result[1][2],
                                   height2=result[1][3],
                                   weight2=result[1][4],
                                   home2=result[1][5],
                                   workplace2=result[1][6],
                                   constellation2=result[1][7],
                                   hobby2=result[1][8],
                                   intro2=result[1][9],
                                   photo_data2=result[1][10],
                                   age3=result[2][0],
                                   grade3=result[2][1],
                                   cate3=result[2][2],
                                   height3=result[2][3],
                                   weight3=result[2][4],
                                   home3=result[2][5],
                                   workplace3=result[2][6],
                                   constellation3=result[2][7],
                                   hobby3=result[2][8],
                                   intro3=result[2][9],
                                   photo_data3=result[2][10],
                                   age4=result[3][0],
                                   grade4=result[3][1],
                                   cate4=result[3][2],
                                   height4=result[3][3],
                                   weight4=result[3][4],
                                   home4=result[3][5],
                                   workplace4=result[3][6],
                                   constellation4=result[3][7],
                                   hobby4=result[3][8],
                                   intro4=result[3][9],
                                   photo_data4=result[3][10],
                                   age5=result[4][4],
                                   grade5=result[4][1],
                                   cate5=result[4][2],
                                   height5=result[4][3],
                                   weight5=result[4][4],
                                   home5=result[4][5],
                                   workplace5=result[4][6],
                                   constellation5=result[4][7],
                                   hobby5=result[4][8],
                                   intro5=result[4][9],
                                    photo_data5=result[1][10],

                                   )
        else:
            # 数字不符合要求，重新渲染表单页面
            return render_template('welcome.html', error='数字不符合要求，请重新输入')
    return render_template('welcome.html', error=None)


@app.route('/getRank', methods=['POST'])
def get_rank():
    data = request.json
    update_data_by_student_id(connection, student_info, list(data.values()))
    # print(data)

    return 'ok'


if __name__ == '__main__':

    # MySQL数据库连接配置

    # # 调用函数检查学号是否存在
    # student_id_to_check = 'your_student_id'
    # result = validate_number(connection, student_id_to_check)
    #
    # # 输出结果
    # if result:
    #     print(f"学号 '{student_id_to_check}' 存在于数据库中。")
    # else:
    #     print(f"学号 '{student_id_to_check}' 不存在于数据库中。")

    app.run()

    # 关闭数据库连接
    if connection.is_connected():
        connection.close()
