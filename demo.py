"""
This module performs several calculations on even numbers up to a given limit.
It includes functions to:
- Calculate the square of a number.
- Check if a number is even.
- Calculate the sum of squares of even numbers up to a given limit.
- Collect even numbers up to a given limit.
"""
# Function to calculate the square of a number
def square(num):
    """
    Calculate and return the square of a number.
    Args:
    num (int or float): The number to square.
    Returns:
    int or float: The square of the given number.
    """
    return num * num

# Function to check if a number is even
def is_even(num):
    """
    Check if the given number is even.
    Args:
    num (int): The number to check.
    Returns:
    bool: True if the number is even, False otherwise.
    """
    return num % 2 == 0

# Function to calculate the sum of squares of even numbers up to a limit
def sum_of_squares_of_evens(limit):
    """
    Calculate the sum of squares of all even numbers from 1 to the given limit.
    Args:
    limit (int): The upper limit for checking even numbers.
    Returns:
    int: The sum of squares of even numbers from 1 to the limit.
    """
    total = 0
    for i in range(1, limit + 1):
        if is_even(i):
            total += square(i)
    return total

# Function to display the result
def display_result(limit, result):
    """
    Display the result of the calculation.
    Args:
    limit (int): The upper limit for the calculation.
    result (int): The result to display.
    """
    print(f"The sum of squares of even numbers from 1 to {limit} is: {result}")

# Function to collect even numbers up to the given limit
def collect_evens(limit):
    """
    Collect and return all even numbers up to a given limit.
    Args:
    limit (int): The upper limit for collecting even numbers.
    Returns:
    list: A list of even numbers from 1 to the limit.
    """
    evens = []
    for i in range(1, limit + 1):
        if is_even(i):
            evens.append(i)
    return evens

# Main function to tie everything together
def main():
    """
    Main function to perform the calculations and display results.
    It calculates the sum of squares of even numbers, the average,
    and the sum of even numbers up to the limit of 10.
    """
    limit = 10
    # Calculate the sum of squares of even numbers
    sum_squares = sum_of_squares_of_evens(limit)
    # Display the result
    display_result(limit, sum_squares)
    # Collect even numbers
    even_numbers = collect_evens(limit)
    print(f"Even numbers from 1 to {limit}: {even_numbers}")

if __name__ == "__main__":
    main()
