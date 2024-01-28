def card_shuffle(lst):
    n = len(lst) // 2
    L1 = lst[:n] # First half of the list
    L2 = lst[n:] # Second half of the list

    result = []
    for i in range(n):
        result.append(L1[i])
        result.append(L2[i])

    return result

# Example usage
original_list = list(range(1, 7))
shuffled_list = card_shuffle(original_list)
print(original_list)
print(shuffled_list)