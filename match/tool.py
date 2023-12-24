
def grade(self, other):
    point = int(100 / len(other.split(',')))
    if(other.__contains__(self)):
        return point
    else:
        return 0

def cate(self, other):
    point = int(100 / len(other.split(',')))
    if (other.__contains__(self)):
        return point * 3
    else:
        return 0



def constellation(self, other):
    if other == '不关心星座':
        return 8
    else:
        if other.__contains__(self):
            return int(100 / len(other.split(',')))
        else:
            return 0


def hobby(self, other):
    # 将两个字符串转换为集合
    set1 = set(self)
    set2 = set(other)
    # 计算集合的交集
    common_characters = set1 & set2
    size = len(set1) + len(set2)
    # 返回交集中元素的数量
    return int(200 * len(common_characters) / size)

def height(self, other):
    det = abs(int(other) - int(self))
    if det <= 5:
        return 100
    else:
        p = 100 - ((det - 5) * 20)
        if p < 0:
            return 0
        else:
            return p

print(height(155, 164))

def bmi(self_height, self_weight, other):
    self = float(self_weight) / (float(self_height)/100 * float(self_height)/100)
    if self < 18.5:
        kind = "轻"
    elif self < 21:
        kind = "偏轻"
    elif 24.9 > self > 21.1:
        kind = "中等"
    elif 27.5 > self > 25:
        kind = "偏重"
    else:
        kind = "重"

    point = int(100 / len(other.split(',')))
    if (other.__contains__(kind)):
        return point
    else:
        return 0



def home(self, other):
    if other.__contains__("没有"):
        return 50
    else:
        pls = other.split('；')
        for i in pls:
            if self.__contains__(i):
                return 100
    return 0

def workplace(self, other):
    if other.__contains__("没有"):
        return 50
    else:
        self = self.split('；')
        num = 0
        for i in self:
            if other.__contains__(i):
                num = num + 1
        fac = len(self) + len(other.split('；'))

        return int(num * 2 / fac * 100)

# import csv
#
# t = open("rawdata.csv", mode="r", encoding="ANSI")
# data1 = csv.DictReader(t)
# datat = []
# for i in data1:
#     datat.append(i)
# f = open("result.csv", mode="r", encoding="ANSI")
# data = csv.reader(f)
#
# for i in data:
#     ct1 = 0
#     ct2 = 0
#     for j in datat:
#         if j['编号'] == i[0] or j['编号'] == i[1]:
#             if j['性别'] == '男':
#                 ct1 = ct1 + 1
#             else:
#                 ct2 = ct2 + 1
#     if not (ct1 == 1 and ct2 == 1):
#         print(i,ct1,ct2)
#
#
