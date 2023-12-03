def has_more_vowels(s):
    # Base case: if the string is empty or has only one character, it does not have more vowels than consonants
    if len(s) <= 1:
        return False
    
    # Helper function to check if a character is a vowel
    def is_vowel(ch):
        vowels = "aeiouAEIOU"
        return ch in vowels
    
    vowel_count = 0
    consonant_count = 0
    if is_vowel(s[0]):
        vowel_count += 1
    else:
        consonant_count += 1

    vowel_count_rest, consonant_count = has_more_vowels(s[1:])

    return(vowel_count + vowel_count_rest) > (consonant_count + consonant_count)