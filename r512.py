def compute_sum(dataset):
    total_sum = sum(sum(row) for row in dataset)
    return total_sum