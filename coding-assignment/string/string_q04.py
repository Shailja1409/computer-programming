'''You have a puzzle where some letters are missing in a word. The missing letters are replaced by underscores (_). Your job is to find out what those letters are, based on a given clue, and replace them in the word.

Problem: Write a Python program that takes a word with underscores and a clue (string of characters that fill the blanks) and prints the complete word.

Example:

Input:
Th_ _at
clue: erc

Output:
The cat'''

def complete_word(word, clue):
    word_list = list(word)  
    clue_index = 0 
    for i in range(len(word_list)):
        if word_list[i] == '_':
            word_list[i] = clue[clue_index]
            clue_index += 1  
    
    print("".join(word_list))

word = "Th_ _at"
clue = "erc"
complete_word(word, clue)
