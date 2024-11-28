'''You are analyzing an essay for repeated words. Your task is to find and print all the words that appear more than once in the essay.

Problem: Write a program that reads a paragraph of text and prints the words that appear more than once.

Example:

Input:
The dog is fast. The dog runs quickly.

Output:
The dog     '''

import string
from collections import Counter

def find_repeated_words(paragraph):
    table = str.maketrans('', '', string.punctuation)
    words = paragraph.translate(table).lower().split()
    
    word_counts = Counter(words)
    
    repeated_words = [word for word, count in word_counts.items() if count > 1]
    
    print(" ".join(repeated_words))

input_paragraph = "The dog is fast. The dog runs quickly."
find_repeated_words(input_paragraph)
