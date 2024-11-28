'''You are reading a poem that has been accidentally jumbled, and the lines are out of order. Your task is to sort the lines of the poem based on the number of words in each line.

Problem: Write a program that takes a list of lines from a poem and sorts them based on the number of words in each line, from shortest to longest.

Example:

Input:
The sky is blue
The night is dark and full of stars
Twinkle twinkle little star

Output:
The sky is blue
Twinkle twinkle little star
The night is dark and full of stars  '''

def sort_poem_lines(lines):
    sorted_lines = sorted(lines, key=lambda line: len(line.split()))
    

    for line in sorted_lines:
        print(line)

input_lines = [
    "The sky is blue",
    "The night is dark and full of stars",
    "Twinkle twinkle little star"
]

sort_poem_lines(input_lines)
