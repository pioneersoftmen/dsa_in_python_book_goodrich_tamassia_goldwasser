from collections import deque

def generate_subsets(T):
    q = deque() # Queue to store subsets]
    S = [] # Stack to generate subsets

    T_list = list(T) # Convert set T to a list

    S.append(set()) # Add an empty set to the stack

    while S:
        subset = S.pop() # Pop the top set from the stack

        q.append(subset) # Enqueue the subset into the queue

        for elem in T_list:
            if elem not in subset:
                new_subset = subset.copy() # Create a new set 
                new_subset.add(elem)
                S.append(new_subset) # Push the new set to the stack

    return q
    
