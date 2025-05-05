def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

if __name__ == "__main__":
    try:
        user_input = int(input("Enter a number: "))
        fizz_buzz(user_input)
    except ValueError:
        print("Please enter a valid integer.")