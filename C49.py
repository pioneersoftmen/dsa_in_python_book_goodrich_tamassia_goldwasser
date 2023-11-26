def find_min_max(sequence):
    if len(sequence) == 1:
        return sequence[0], sequence[0]
    elif len(sequence) == 2:
        return (sequence[0], sequence[1]) if sequence[0] < sequence[1] else (sequence[1], sequence[0])
    else:
        mid = len(sequence) // 2
        left_min, left_max = find_min_max(sequence[mid:])
        right_min, right_max = find_min_max(sequence[mid:])
        return min(left_min, right_min), max(left_max, right_max)
    
my_sequence = [5, 3, 8, 2, 9, 1]
min_value, max_value = find_min_max(my_sequence)
print("Minimum value: ", min_value)
print("Maximum value: ", max_value)