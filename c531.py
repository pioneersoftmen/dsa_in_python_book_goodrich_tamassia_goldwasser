def sum_arr(dataset):
    if len(dataset) == 1:
        return sum(dataset[0])
    else:
        return sum(dataset[0]) + sum_arr(dataset[1:])
dataset = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


print(sum_arr(dataset))


