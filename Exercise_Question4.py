from collections import Counter

def count_repeated_characters(s):
 
    char_count = Counter(s)
    repeated_chars = {char: count for char, count in char_count.items() if count > 1}
    return repeated_chars

if __name__ == "__main__":
    input_string = input("Enter a string to find repeated characters: ")
    result = count_repeated_characters(input_string)
    print(f"Repeated characters and their counts: {result}")