'''You are working at a name badge company, and you need to print out names in reverse order for a special event. The names are entered as "First Last", and you need to print them as "Last First".

Problem: Write a Python program that takes a list of names in "First Last" format and prints them in "Last First" format.

Example:

Input:
John Doe Alice Johnson

Output:
Doe John Johnson Alice'''

def reverse_names(names):
    name_list = names.split()
  
    reversed_names = []
  
    for i in range(0, len(name_list), 2):
        first_name = name_list[i]
        last_name = name_list[i + 1]
        # Reverse the name order and add to the result list
        reversed_names.append(f"{last_name} {first_name}")
  
    print(" ".join(reversed_names))
  
input_names = "John Doe Alice Johnson"
reverse_names(input_names)
