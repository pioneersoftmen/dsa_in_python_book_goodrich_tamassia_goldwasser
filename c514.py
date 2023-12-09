import random

def custom_shuffle(lst):
    for i in range(len(lst) - 1, 0, -1):
        j = random.randrange(0, i + 1)
        lst[i], lst[j] = lst[j], lst[i]
    return lst


my_list = [1, 2, 3, 4, 5] 
shuffled_list = custom_shuffle(my_list)
print(shuffled_list)