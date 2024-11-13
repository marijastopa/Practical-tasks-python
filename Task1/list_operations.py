def process_numbers(numbers):
    # Remove duplicates by converting to a set and then back to a tuple
    unique_numbers = tuple(set(numbers))
    
    # Notify if all elements are duplicates of a single number
    if len(unique_numbers) == 1:
        print("Warning: Only one unique number was entered.")
        return unique_numbers, unique_numbers[0], unique_numbers[0]

    # Find the minimum and maximum values in the tuple
    min_number = min(unique_numbers)
    max_number = max(unique_numbers)
    return unique_numbers, min_number, max_number

if __name__ == "__main__":
    # Limit on the maximum number of elements
    MAX_INPUT_SIZE = 100  # Define as needed
    
    # Input list of numbers as space-separated values
    input_numbers = input("Enter integers separated by spaces: ").split()
    
    # Check if input is empty
    if not input_numbers:
        print("Error: No input provided. Please enter at least one integer.")
        exit(1)
    
    # Check if input exceeds maximum size
    if len(input_numbers) > MAX_INPUT_SIZE:
        print(f"Error: Input exceeds maximum size of {MAX_INPUT_SIZE} elements.")
        exit(1)
    
    try:
        # Convert each input value to an integer
        numbers = [int(num) for num in input_numbers]
    except ValueError:
        print("Error: All inputs must be integers.")
        exit(1)
    
    # Process numbers to remove duplicates and find min/max
    unique_numbers, min_number, max_number = process_numbers(numbers)
    
    # Print the results
    print(f"Unique numbers as tuple: {unique_numbers}")
    print(f"Minimum: {min_number}, Maximum: {max_number}")

