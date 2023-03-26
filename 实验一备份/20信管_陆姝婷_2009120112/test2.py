import numpy as np
import math


class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        a = np.array((self.x, self.y))
        return a.shape[0]

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __scale__(self, other):
        x = self.x * other.x
        y = self.y * other.y
        return Vector(x, y)

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __str__(self):
        return "Vector({},{})".format(self.x, self.y)


def main():
    v1 = Vector(2, 4)
    v2 = Vector(3, 8)

    print(f"第一个向量维度：{v1.__len__()}")
    print(f"第二个向量维度：{v2.__len__()}")
    print("第一个向量元素：" + v1.__str__())
    print("第二个向量元素：" + v2.__str__())
    v3 = v1 + v2
    print(f"两个向量相加为：{v3}")
    v4 = v1.__scale__(v2)
    print(f"两个向量内积为：{v4}")


if __name__ == '__main__':
    main()
