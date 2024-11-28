'''The task is to perform the operation of removing all the occurrences of a given item/element present in a list. 

Example

Input1: 1 1 2 3 4 5 1 2 1 
Output1: 2 3 4 5 2 
Explanation : The input list is [1, 1, 2, 3, 4, 5, 1, 2] and the item to be removed is 1. 
 After removing the item, the output list is [2, 3, 4, 5, 2]  '''


def remove_items(test_list, item): 
  
    # using list comprehension to perform the task 
    res = [i for i in test_list if i != item] 
    return res 
  
# driver code 
if __name__ == "__main__": 
    test_list = [1, 3, 4, 6, 5, 1] 
    # the item which is to be removed 
    item = 1
    print("The original list is : " + str(test_list)) 
  
    # calling the function remove_items() 
    res = remove_items(test_list, item) 
  
    # printing result 
    print("The list after performing the remove operation is : " + str(res)) 

