'''Given a dictionary, perform append of keys followed by values in list.


Input : test_dict = {“Gfg” : 1, “is” : 2, “Best” : 3} 
Output : ['Gfg', 'is', 'Best', 1, 2, 3] 
Explanation : All the keys before all the values in list. 


Input : test_dict = {“Gfg” : 1, “Best” : 3} 
Output : ['Gfg', 'Best', 1, 3] 
Explanation : All the keys before all the values in list.'''


test_dict = {"Gfg" : 1, "is" :  3, "Best" : 2}
 
# printing original dictionary
print("The original dictionary is : " + str(test_dict))
 
# + operator is used to perform adding keys and values
res = list(test_dict.keys()) + list(test_dict.values())
 
# printing result 
print("The ordered keys and values : " + str(res)) 
