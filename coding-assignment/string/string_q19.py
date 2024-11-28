'''Your friend has sent you a long email where none of the sentences start with a capital letter. To make the email look nicer, you want to capitalize the first letter of each sentence.

Problem: Write a Python program that takes a paragraph of text and capitalizes the first letter of each sentence.

Example:

Input:
hello. my name is john. i love programming.

Output:
Hello. My name is John. I love programming.  '''

def capitalize_sentences(paragraph):
    # Split the paragraph into sentences using the period as a delimiter
    sentences = paragraph.split(". ")
    
    # Capitalize the first letter of each sentence and reassemble the paragraph
    capitalized_sentences = [sentence.capitalize() for sentence in sentences]
    
    # Join the sentences back into a single string, adding the period back
    result = ". ".join(capitalized_sentences)
    
    # Ensure that the paragraph ends with a period if the original had one
    if paragraph.endswith("."):
        result += "."
    
    # Print the result
    print(result)

# Test the function with the provided example
input_paragraph = "hello. my name is john. i love programming."
capitalize_sentences(input_paragraph)
