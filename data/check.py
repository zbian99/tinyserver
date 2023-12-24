import csv

import csv

# 打开 CSV 文件
with open('delete_student_number.csv', 'r', encoding="utf-8") as file:
    # 创建 CSV 读取器
    csv_reader = csv.reader(file)
    # with open('delete_student_number.csv', 'w', newline='', encoding="utf-8") as output_file:
    #     # 创建 CSV 写入器
    #     csv_writer = csv.writer(output_file)
    line = 1
    # 逐行遍历 CSV 文件
    for row in csv_reader:
        print(row)
        line = line + 1

