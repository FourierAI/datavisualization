class Vector:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return str(self.data)

    def __add__(self, other):
        if len(self.data) != len(other.data):
            raise ValueError("向量必须是同一维度")
        result = []
        for i in range(len(self.data)):
            result.append(self.data[i] + other.data[i])
        return Vector(result)

    def dot(self, other):
        if len(self.data) != len(other.data):
            raise ValueError("向量必须是同一维度")
        result = 0
        for i in range(len(self.data)):
            result += self.data[i] * other.data[i]
        return result


X = Vector([1, 2, 3, 5])
Y = Vector([2, 5, 8, 6])
print(len(X))
print(X)
print(X + Y)
print(X.dot(Y))

