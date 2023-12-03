def subsets(arr):
    if len(arr) == 0:
        return [[]] # Base case: empty set has one subset, which is an empty set itself
    
    subsets_without_first = subsets(arr[1:]) # Recursive call to get subsets of remaining elements
    subsets_with_first = [[arr[0]] + subset for subset in subsets_without_first] # Include first element in each subset

    return subsets_without_first + subsets_with_first # Combine subsets without first and with first

elements = [1, 2, 3]
result = subsets(elements)
for subset in result:
    print(subset)
    