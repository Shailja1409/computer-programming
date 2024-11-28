'''Checking if a list contains elements within a specific range is a common problem'''

a = [3, 8, 12, 18, 25]

#Define the range
start, end = 10, 20

# Check if any element in the list is in the range
in_range = any(start <= num <= end for num in a)

print(in_range)
