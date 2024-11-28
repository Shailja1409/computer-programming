'''Write a program that takes a list of names, rearranges them so that names starting with a vowel come first, and then prints the rearranged list.

Example:

Input:
Alice Bob Uma Charlie Eve

Output:
Alice Uma Eve Bob Charlie'''


def rearrange_names(names):
    vowels = "AEIOUaeiou"
    
    names_list = names.split()
    
    vowel_names = [name for name in names_list if name[0] in vowels]
    consonant_names = [name for name in names_list if name[0] not in vowels]
    
    rearranged_list = vowel_names + consonant_names
    
    print(" ".join(rearranged_list))

input_names = "Alice Bob Uma Charlie Eve"
rearrange_names(input_names)
