#Function to Find the First Non-Repeated Character in a String

def first_non_repeated_char(s):
    from collections import Counter
    count = Counter(s)
    for char in s:
        if count[char] == 1:
            return char
    return None
