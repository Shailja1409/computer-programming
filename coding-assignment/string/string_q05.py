'''In a small village, there are many people with the same names. You have a list of names of people in the village, and your task is to remove the duplicates and print only the unique names.

Problem: Write a Python program that takes a list of names and removes any duplicates, then prints the unique names.

Example:

Input:
John Mary John Alex Alex

Output:
John Mary Alex'''

def remove_duplicates(names):
    seen = set()  
    unique_names = []  
    
    for name in names.split():
        if name not in seen:
            unique_names.append(name)
            seen.add(name)
    
    print(" ".join(unique_names))

input_names = "John Mary John Alex Alex"
remove_duplicates(input_names)
