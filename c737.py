def find_pair_with_sum(positional_list, V):
    if len(positional_list) < 2:
        return None
    
    start = positional_list.first()
    end = positional_list.last()

    while start != end:
        current_sum = start.element() + end.element()

        if current_sum == V:
            return start, end
        elif current_sum < V:
            start = positional_list.after(start)
        else:
            end = positional_list.before(end)
    
    return None