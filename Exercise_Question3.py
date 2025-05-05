def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    return sum(1 for char in input_string if char in vowels)

if __name__ == "__main__":
    user_input = input("Enter a string to count the vowels: ")
    print(f"Number of vowels: {count_vowels(user_input)}")