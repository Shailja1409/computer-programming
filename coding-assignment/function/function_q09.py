#Flatten a Nested List
#Question: Write a function to flatten a nested list.
Solution:


def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]

# Example
result = flatten_list([[1, 2], [3, 4], [5]])
print(result)  # Output: [1, 2, 3, 4, 5]
