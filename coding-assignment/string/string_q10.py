'''You have received a confusing message from your friend. The words in the message are all jumbled up. You need to reverse the order of the words to understand the message properly.

Problem: Write a program that takes a sentence and reverses the order of the words.

Example:

Input:
I love programming

Output:
programming love I'''

def reverse_sentence(sentence):
    words = sentence.split()
    
    reversed_words = words[::-1]
    
    print(" ".join(reversed_words))

input_sentence = "I love programming"
reverse_sentence(input_sentence)
