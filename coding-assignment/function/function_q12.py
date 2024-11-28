#Find the Average
#Question: Write a function to find the average of a list of numbers.

#Solution:


def find_average(lst):
    return sum(lst) / len(lst) if len(lst) > 0 else 0

# Example
result = find_average([1, 2, 3, 4, 5])
print(result)  # Output: 3.0
