'''You are playing a word puzzle game where you need to find the shortest word in a sentence. Your task is to write a program that can help you find the shortest word.

Problem: Write a program that takes a sentence and prints the shortest word in the sentence.

Example:

Input:
I love playing games

Output:
I          '''

def find_shortest_word(sentence):
    words = sentence.split()
    
    shortest_word = min(words, key=len)
    
    print(shortest_word)

input_sentence = "I love playing games"
find_shortest_word(input_sentence)
