def transfer(S, T):
    while not S.is_empty():
        T.push(S.pop())