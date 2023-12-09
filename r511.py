def compute_sum(dateset):
    total_sum = 0
    for row in dateset:
        for number in row:
            total_sum += number
    return total_sum

dataset = [
    [1, 2, 3],
    [4, 5, 6], 
    [7, 8, 9]
]
 
total_sum = compute_sum(dataset)
print(total_sum)