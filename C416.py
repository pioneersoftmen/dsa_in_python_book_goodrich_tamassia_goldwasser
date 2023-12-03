s = input()
def reverser(s):

    if len(s) <= 1:
        return s
    return s[-1] + reverser(s[:-1])

print(reverser(s)) 