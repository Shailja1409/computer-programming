'''You are working on a school project where you need to analyze a paragraph of text. Your task is to count the number of words in the paragraph.

Problem: Write a program that takes a paragraph of text and prints the total number of words.

Example:

Input:
This is a sample text for testing.

Output:
6          '''

def count_words(paragraph):
    words = paragraph.split()
    
    word_count = len(words)
    
    print(word_count)

input_paragraph = "This is a sample text for testing."
count_words(input_paragraph)


