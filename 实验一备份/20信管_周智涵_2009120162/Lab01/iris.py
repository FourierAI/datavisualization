from collections import Counter
import random
import numpy as np

with open("iris.data", "r") as file:
    iris_list = []
    # ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]
    for line in file:
        line = line.replace("\n", "")  # 去除掉换行
        col = line.split(",")  # 将数据拆分为列表
        iris_list.append(col)  # 添加进iris_list

print("共有样本个数：" + str(len(iris_list)))
species = Counter(row[4] for row in iris_list)  # 调用counter函数方法统计类别
print(species)
sorted_ls = sorted(iris_list, key=lambda x: x[0])  # 以第一列为关键字排序
print(sorted_ls)


def sampling_with_replacement(data, number):  # 有放回
    return random.choices(data, k=number)


def sampling_without_replacement(data, number):  # 无放回
    return random.sample(data, k=number)


print(sampling_with_replacement(iris_list, 10))
print(sampling_without_replacement(iris_list, 10))

iris_list = [lst[:-1] for lst in iris_list]  # 去除最后一列名称
float_iris_list = []  # 将由于split，字符串转换为浮点数
for tmp in iris_list:
    for item in tmp:
        float_iris_list.append(float(item))

float_iris_list = [float_iris_list[i:i + 4] for i in range(0, len(float_iris_list), 4)]  # 切片每四个分一组
print(float_iris_list)
iris_list = np.array(float_iris_list)
mean = np.mean(iris_list, axis=0)  # 平均数
variance = np.var(iris_list, axis=0)  # 方差
std_deviation = np.std(iris_list, axis=0)  # 标准差
median = np.median(iris_list, axis=0)  # 中位数
print(mean)
print(variance)
print(std_deviation)
print(median)
