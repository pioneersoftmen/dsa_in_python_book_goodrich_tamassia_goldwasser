def caesar_cipher(message, shift):
    ciphered_message = ""

    for char in message:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            ciphered_char = chr((ord(char) - start + shift) % 26 + start)
            ciphered_message += ciphered_char
        else:
            ciphered_message += char

    return ciphered_message

