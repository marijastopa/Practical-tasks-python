# Task1 
# 1. File Extension Checker

This Python script checks for the file extension of a given filename. If there is no extension or if the input is invalid, the script raises an appropriate error.

## Requirements

- Python 3.x

## Usage
1. Open a terminal and navigate to the directory where ``file_extension_checker.py`` is located.

2. Run the script with:
```python3 file_extension_checker.py```

3. Enter a filename when prompted. The script will:
- Print the file extension if it exists.
- Raise an error if there is no extension or if the input is invalid.

### Example
```
$ python3 file_extension_checker.py
Enter the file name: example.txt
File extension: txt
```

## Edge Cases
The script handles the following edge cases:
- **Empty Input:** Raises an error if no input is provided.
- **Spaces Only:** Raises an error if only spaces are entered.
- **No Extension:** Raises an error if there’s no extension, e.g., example.
- **Ends with a Dot:** Raises an error if the filename ends with a dot, e.g., example..

## Error Handling
The script provides clear error messages for invalid inputs:
- "Filename cannot be empty or only spaces."
- "Invalid filename: No extension found."

# 2. List Operations Script

This Python script removes duplicate integers from a list, converts the list to a tuple of unique values, and calculates the minimum and maximum values. The script also includes robust error handling for various edge cases.

## Usage
1. Open a terminal and navigate to the directory where list_operations.py is located.
2. Run the script with:
```python3 list_operations.py```
3. Enter a list of integers separated by spaces when prompted. The script will:
- Remove duplicates and display the unique integers as a tuple.
- Calculate and display the minimum and maximum values from the unique numbers.

## Example
```
$ python3 list_operations.py
Enter integers separated by spaces: 5 3 8 3 2 9 5
Unique numbers as tuple: (2, 3, 5, 8, 9)
Minimum: 2, Maximum: 9
```

## Error Handling
The script includes error handling for the following cases:
- **Empty Input:** If no input is provided, an error message appears.
- **Non-Integer Input:** If any input is not an integer, an error message appears.
- **Single Unique Number:** If the list only contains one unique number, a warning appears, and both min and max are set to that value.
- **Input Exceeding Maximum Size:** If more than 100 numbers are entered, an error message appears.

## Testing
Use the following test cases to verify the functionality and error handling of the script:
**1. Valid Input with Mixed Numbers**
- Input: 5 3 8 3 2 9 5
- Expected Output: (2, 3, 5, 8, 9), Minimum: 2, Maximum: 9
  
**2. All Duplicate Numbers**
- Input: 5 5 5 5
- Expected Output: (5,), Warning message
  
**3. Two Unique Numbers**
- Input: 10 10 5 5
- Expected Output: (10, 5), Minimum: 5, Maximum: 10
  
**4. Empty Input**
- Expected Output: Error message

**5. Non-Integer Input**
- Input: 5 3 abc 8
- Expected Output: Error message

**6. Input Exceeding Maximum Size**
- Input: 101 numbers
- Expected Output: Error message
  
**7. Spaces Only**
- Input: Spaces only
- Expected Output: Error message

# 3. Access Log Analyzer

This Python script analyzes an HTTP access log file to count unique User Agents and the number of requests associated with each User Agent. It is helpful for summarizing request patterns and understanding the diversity of User Agents accessing a web service.

## Usage
1. Open a terminal and navigate to the directory containing access_log_analyzer.py.
2. Run the script by specifying the path to the log file as an argument:

        python3 access_log_analyzer.py <path_to_log_file>


Replace ``<path_to_log_file>`` with the path to your log file. For example:

         python3 access_log_analyzer.py ~/Downloads/access.log.5

3. Expected Output:
The script will display:
 - The total number of unique User Agents.
- A count of requests from each User Agent found in the log file.
  
### Example Output
```
Total unique User Agents: 31
Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/8888 Safari/537.36: 1
Mozilla/5.0: 2
python-requests/2.22.0: 1
-: 17
```

In this example:
- ``Total unique User Agents: 31`` indicates that 31 unique User Agents were found.
- Each User Agent is listed with its request count (e.g., ``Mozilla/5.0: 2`` means this User Agent made 2 requests).
- The entry ``-: 17`` indicates 17 requests with no User Agent information available (represented by ``-``).

## Error Handling
The script includes error handling for various cases:
- **File Not Found:** If the specified file does not exist, an error message will appear:
  
  ``Error: File not found. Please check the file name and try again.``
- **Permission Error:** If the file cannot be read due to permissions, an error message will appear:

  ``Error: Permission denied. Please check file permissions.``
- **Empty File:** If the log file is empty, the script will display:
  
  ``Error: The file is empty.``
- **Malformed Lines:** If some lines in the log do not contain a User Agent, the script will skip those lines and continue processing valid entries.
- **Empty or Invalid User Agents:** The script excludes empty or whitespace-only User Agent entries from the results.

# 4. Character Occurrence Counter

This Python script counts the occurrences of each character in a given input string. It provides a breakdown of how many times each character appears, including letters, numbers, spaces, and special characters.

## Usage
1. Open a terminal and navigate to the directory containing char_counter.py.
2. Run the script with:
```python3 char_counter.py```
3. When prompted, enter a string. The script will output each character and its count.

### Example Output
```
$ python3 char_counter.py
Enter a string: pythonnohtyppy
p: 3
y: 3
t: 2
h: 2
o: 2
n: 2
```

In this example:
- The character ``p`` appears 3 times, ``y`` appears 3 times, etc.

## Error Handling
The script includes error handling for:
- **Empty Input:** If no input is provided or only whitespace is entered, the script will display an error message:
  
``Error: No input provided. Please enter a non-empty string.``


## Testing
To verify the script's functionality, you can try the following test cases:
- **Standard Input:** ``pythonnohtyppy`` – should show counts for each letter.
- **Input with Spaces and Special Characters:** ``hello world!`` – should count spaces and special characters.
- **Empty Input:** Press Enter without typing anything – should display an error.
- **Whitespace Only:** ``" "`` – should also display an error.
- **Numeric Input:** ``123321`` – should count numbers as characters.
- **Long Input with Repeats:** ``aaaaaaabbbbcccc`` – should count repeated characters accurately.

# 5. System Information Script
This Python script retrieves and displays various system information based on specified command-line arguments. It provides details such as distribution info, memory usage, CPU details, current user, system load average, and IP address.

## Usage
1. Open a terminal and navigate to the directory containing system_info.py.
2. Run the script with any combination of the following flags to retrieve specific information:
- ``-d`` : Distribution information
- ``-m`` : Memory information (total, used, free)
- ``-c`` : CPU information (model, core count, speed)
- ``-u`` : Current user
- ``-l`` : System load average
- ``-i`` : IP address

## Example Commands:
- To view distribution information:
```python3 system_info.py -d```


- To view memory and CPU information together:
```python3 system_info.py -m -c```


- To display all available information:
```python3 system_info.py -d -m -c -u -l -i```

### Example Output
```
$ python3 system_info.py -d -m -c
Distro Info: Linux-5.4.0-42-generic-x86_64-with-Ubuntu-20.04-focal
Memory Info: Total: 16777216, Used: 8388608, Free: 8388608
CPU Info: CPU: Intel(R) Core(TM) i7-8550U CPU @ 1.80GHz, Cores: 4, Speed: 1992.0 MHz
```

If the IP address cannot be retrieved due to network configuration issues, the output will be:

``IP Address: IP Address information unavailable. Please check your network connection.``

## Error Handling
The script includes basic error handling:
- **IP Address Unavailability:** If the system cannot resolve the hostname to an IP address, a message will indicate that the IP address is unavailable.
- **Missing psutil Library:** If psutil is not installed, an error message will prompt the user to install it.

## Testing
You can test each of the arguments individually or in combination to verify the script's functionality. Examples of test cases include:
- Running with ``-d`` for distribution info
- Running with ``-m -c -l`` for memory, CPU, and load average info
- Running with all flags (``-d -m -c -u -l -i``) to ensure the script outputs each detail as expected.
































