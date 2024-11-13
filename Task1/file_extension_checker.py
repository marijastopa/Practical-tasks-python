def get_file_extension(filename):
    # Check if the filename is empty or only contains spaces
    if not filename.strip():
        raise ValueError("Filename cannot be empty or only spaces.")
    # Check if there's a dot in the filename
    if '.' not in filename or filename.endswith('.'):
        raise ValueError("Invalid filename: No extension found.")
    # Return the part of the filename after the last dot
    return filename.split('.')[-1]

if __name__ == "__main__":
    # Ask the user to input the filename
    filename = input("Enter the file name: ")
    try:
        # Try to get the file extension and print it
        extension = get_file_extension(filename)
        print(f"File extension: {extension}")
    except ValueError as e:
        # If there's no extension, print the error message
        print("Error:", e)

