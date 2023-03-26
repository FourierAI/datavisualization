import random

import numpy as np

fp = open("iris.data")
iris_data = fp.readlines()
print(iris_data)
iris_length = len(iris_data)
print(f"含样本数：{iris_length}")

print("===================================================")

count = 1
list = []
iris_list = []
for i in range(iris_length):
    iris_list.append(iris_data[i].split(","))
print(iris_list)
list.append(iris_list[0][4].replace('\n', ''))


def fun1(list, data):
    for i in range(len(list)):
        if list[i] == data:
            return False
    list.append(data)
    return True


for i in range(iris_length):
    if fun1(list, iris_list[i][4].replace('\n', '')):
        count = count + 1

print(list)
print(f"iris.data中有类别：{count}")

print("===================================================")

iris_list.sort(key=(lambda x: float(x[0])), reverse=False)
print("按照第一列升序排序结果：")
for i in range(iris_length):
    print(iris_list[i])

print("===================================================")


# 放回随机抽样
def sampling_with_replacement(data, number):
    for i in range(number):
        print(random.choice(data))


print("有放回随机抽样8个为：")
sampling_with_replacement(iris_list, 8)

print("===================================================")


# 无放回随机抽样
def sampling_without_replacement(data, number):
    print(random.sample(data, number))


print("无放回随机抽样6个为：")
sampling_without_replacement(iris_list, 6)

print("===================================================")


def avg(data, line):
    sum = 0
    for i in range(len(data)):
        sum += float(data[i][line - 1])
    return sum / iris_length


line1 = avg(iris_list, 1)
print("第一列的均值：%f" % line1)
line2 = avg(iris_list, 2)
print("第一列的均值：%f" % line2)
line3 = avg(iris_list, 3)
print("第一列的均值：%f" % line3)
line4 = avg(iris_list, 4)
print("第一列的均值：%f" % line4)

print("===================================================")

iris_list_new = []
for i in range(iris_length):
    iris_list_new.append(iris_list[i][0:-1])
    iris_list_new[i] = [float(x) for x in iris_list_new[i]]

np_var1 = np.var(iris_list_new, axis=0, dtype=np.float64)
print(f"前四列的方差：{np_var1}")

print("===================================================")

np_std = np.std(iris_list_new, axis=0)
print(f"前四列的标准差：{np_std}")

print("===================================================")

np_percentile = np.percentile(iris_list_new, 50, axis=0)
print(f"前四列的中位数：{np_percentile}")

fp.close()
