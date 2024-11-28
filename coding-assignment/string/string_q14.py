'''You and your friend are making separate shopping lists for a party. You want to merge the two lists, but you need to remove any duplicate items.

Problem: Write a Python program that takes two lists of items and merges them, removing any duplicates.

Example:

Input:
List 1: apples bananas oranges
List 2: bananas grapes apples

Output:
apples bananas oranges grapes'''

def merge_lists(list1, list2):
    merged_list = list(set(list1 + list2))
    
    print(" ".join(merged_list))

list1 = ["apples", "bananas", "oranges"]
list2 = ["bananas", "grapes", "apples"]
merge_lists(list1, list2)
