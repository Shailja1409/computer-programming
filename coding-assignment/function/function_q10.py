#Count Occurrences of Character
#Question: Write a function to count the number of times a character appears in a string.

#Solution:


def count_char(s, char):
    return s.count(char)

# Example
result = count_char("hello", "l")
print(result)  # Output: 2
