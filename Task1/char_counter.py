from collections import Counter

def count_characters(input_string):
    # Count occurrences of each character
    return Counter(input_string)

if __name__ == "__main__":
    # Prompt the user for input
    input_string = input("Enter a string: ").strip()
    
    # Check if the input is empty after stripping whitespace
    if not input_string:
        print("Error: No input provided. Please enter a non-empty string.")
    else:
        # Get the character counts
        char_counts = count_characters(input_string)
        
        # Display each character and its count
        for char, count in char_counts.items():
            print(f"{char}: {count}")

