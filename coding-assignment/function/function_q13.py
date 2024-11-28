#Count Words
#Question: Write a function to count the number of words in a string.
solution:

python
def count_words(s):
    return len(s.split())

# Example
result = count_words("hello world")
print(result)  # Output: 2
