'''You have received an email, but none of the sentences start with a capital letter. To make the email look professional, you need to capitalize the first letter of each sentence.

Problem: Write a program that takes a paragraph of text and capitalizes the first letter of each sentence.

Example:

Input:
hello there. this is a test.

Output:
Hello there. This is a test.'''

import re

def capitalize_sentences(paragraph):
    sentences = re.split('([.!?])', paragraph)  
    capitalized_sentences = []
    
    for i in range(0, len(sentences)-1, 2):  
        sentence = sentences[i].strip() 
        if sentence: 
            capitalized_sentences.append(sentence[0].upper() + sentence[1:] + sentences[i+1])
    
    result = "".join(capitalized_sentences).strip() 
    print(result)

input_paragraph = "hello there. this is a test."
capitalize_sentences(input_paragraph)
