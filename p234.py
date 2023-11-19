import matplotlib.pyplot as plt
import string

def generate_bar_chart(document):
    # Remove punctuation and convert to lowercase
    document = document.translate(str.maketrans(",", string.punctuation)).lower()
    # Count the frequency of each alphabet character
    freq_dict = {}
    for char in document:
        if char.isalpha():
            freq_dict[char] = freq_dict.get(char, 0) + 1
    # Sort the characters by frequency in decending order
    sorted_chars = sorted(freq_dict.items(), key=lambda x:x[1], reverse = True)
    chars, frequencies = zip(*sorted_chars)

    # Generate the bar char plot
    x_pos = range(len(chars))
    plt.bar(x_pos, frequencies, align='center')
    plt.xticks(x_pos, chars)
    plt.xlabel('Alphabet Character')
    plt.ylabel('Frequency')
    plt.title('Frequency of Alphabet Characters in Document')
    plt.show()

document = input("Enter the document:")

generate_bar_chart(document)

