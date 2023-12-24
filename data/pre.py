import csv

import csv

# 打开 CSV 文件
with open('rawdata.csv', 'r', encoding="utf-8") as file:
    # 创建 CSV 读取器
    csv_reader = csv.reader(file)
    with open('delete_student_number.csv', 'w', newline='', encoding="utf-8") as output_file:
        # 创建 CSV 写入器
        csv_writer = csv.writer(output_file)
        line = 1
        # 逐行遍历 CSV 文件
        for row in csv_reader:
            # 在这里对每一行进行处理
              # 示例：打印每一行的数据
            if len(row[1]) != 8 and len(row[1]) != 12:
                print(line, row)
            else:
                csv_writer.writerow(row)
            line = line + 1

