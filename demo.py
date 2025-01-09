# Function to calculate the square of a number
def square(num):
    return num * num

# Function to check if a number is even
def is_even(num):
    return num % 2 == 0

# Function to calculate the sum of squares of even numbers up to a limit
def sum_of_squares_of_evens(limit):
    total = 0
    for i in range(1, limit + 1):
        if is_even(i):
            total += square(i)
    return total

# Function to display the result
def display_result(limit, result):
    print(f"The sum of squares of even numbers from 1 to {limit} is: {result}")

# Function to calculate the average of numbers in a given list
def average(numbers):
    return sum(numbers) / len(numbers)

# Function to collect even numbers up to the given limit
def collect_evens(limit):
    evens = []
    for i in range(1, limit + 1):
        if is_even(i):
            evens.append(i)
    return evens

# Function to calculate the sum of even numbers up to a given limit
def sum_of_evens(limit):
    evens = collect_evens(limit)
    return sum(evens)

# Main function to tie everything together
def main():
    limit = 10

    # Calculate the sum of squares of even numbers
    sum_squares = sum_of_squares_of_evens(limit)
    
    # Display the result
    display_result(limit, sum_squares)
    
    # Collect even numbers
    even_numbers = collect_evens(limit)
    print(f"Even numbers from 1 to {limit}: {even_numbers}")
    
    # Calculate and display the average of even numbers
    avg = average(even_numbers)
    print(f"Average of even numbers from 1 to {limit}: {avg:.2f}")
    
    # Calculate and display the sum of even numbers
    even_sum = sum_of_evens(limit)
    print(f"Sum of even numbers from 1 to {limit}: {even_sum}")

if __name__ == "__main__":
    main()
