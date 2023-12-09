def add_datasets(dataset1, dataset2):
    result = []
    for i in range(len(dataset1)):
        row = []
        for j in range(len(dataset1[i])):
            component_sum = dataset1[i][j] + dataset2[i][j]
            row.append(component_sum)
        result.append(row)
    return result

dataset1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
dataset2 = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]

result_dataset = add_datasets(dataset1, dataset2)
print(result_dataset)
