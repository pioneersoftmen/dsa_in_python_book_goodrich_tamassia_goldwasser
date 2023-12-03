def is_palindrome(s):
    # Base case: if the string is empty or has only one character, it is considered a palindorome
    if len(s) <= 1:
        return True
    
    # Recursive case: check if the first and last characeters are the same,
    # and recursively call the function on the remaining substring
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False

print(is_palindrome("race"))