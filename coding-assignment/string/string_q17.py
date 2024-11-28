'''You are tracking buses in a busy city, and each bus has a unique number. However, some of the bus numbers have been entered with spaces between the digits. You need to remove the spaces so that you can process the bus numbers correctly.

Problem: Write a Python program that takes a string of bus numbers with spaces and removes the spaces between the digits.

Example:

Input:
Bus numbers: 1 2 3  4 5 6  7

Output:
1234567   '''

def remove_spaces(bus_numbers):
    cleaned_numbers = bus_numbers.replace(" ", "")
    
    print(cleaned_numbers)

input_bus_numbers = "1 2 3  4 5 6  7"
remove_spaces(input_bus_numbers)
