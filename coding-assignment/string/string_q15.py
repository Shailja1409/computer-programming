'''Your friend is creating a website for movies and wants to display all movie titles in title case (where the first letter of each word is capitalized). However, the movie titles are all in lowercase. Your job is to help your friend by writing a program that converts the movie titles to title case.

Problem: Write a Python program that takes a list of movie titles in lowercase and converts them to title case.

Example:

Input:
the lord of the rings harry potter

Output:
The Lord Of The Rings Harry Potter'''

def convert_to_title_case(titles):
    title_case_titles = titles.title()
    
    print(title_case_titles)

input_titles = "the lord of the rings harry potter"
convert_to_title_case(input_titles)
