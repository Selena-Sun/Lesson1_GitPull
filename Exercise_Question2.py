def sum_of_squares(numbers):
    return sum(x ** 2 for x in numbers)

if __name__ == "__main__":
    user_input = input("Enter a list of numbers in the format [a, b, c, d]: ")
    # Remove brackets and split the input by commas
    numbers = list(map(float, user_input.strip("[]").split(",")))
    result = sum_of_squares(numbers)
    print(f"The sum of the squares of the numbers is: {result}")