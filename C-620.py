def enumerate_permutations(n):
    S = [] # Stack to store permutations
    result = [] # List to store all permutations

    S.append([1]) # Add the initial permutation[1] to the stack 

    while S:
        perm = S.pop() # Pop the top permutation from the stack

        if len(perm) == n: # If the permutation is complete
            result.append(perm) # Add it to the result list
        else:
            for num in range(n, 0, -1): # Loop from n to 1 in reverse order
                if num not in perm: # If num is not in the current permutation
                    new_perm = perm + [num] # Create a new permutation 
                    S.append(new_perm) # Push the new permutation to the stack

    return result