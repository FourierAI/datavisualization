# tmp_sum = 0
# count_ = 0
# with open("iris.data", "r") as file:
#     for line in file:
#         cols = line.split(",")
#         sepal_length = cols[0]
#         sepal_length = float(sepal_length)
#         tmp_sum += sepal_length
#         count_ += 1
# print(f"mean:{tmp_sum/count_}")


sepal_lengths = []
with open("iris.data", "r") as file:
    for line in file:
        cols = line.split(",")
        sepal_length = cols[0]
        sepal_length = float(sepal_length)
        sepal_lengths.append(sepal_length)
print(f"mean:{sum(sepal_lengths)/len(sepal_lengths)}")