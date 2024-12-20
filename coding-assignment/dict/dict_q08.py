'''Given String, replace it's words from lookup dictionary.


Input : test_str = 'geekforgeeks best for geeks', repl_dict = {“geeks” : “all CS aspirants”} 
Output : geekforgeeks best for all CS aspirants 
Explanation : “geeks” word is replaced by lookup value. 


Input : test_str = 'geekforgeeks best for geeks', repl_dict = {“good” : “all CS aspirants”} 
Output : geekforgeeks best for geeks 
Explanation : No lookup value, unchanged result.'''

test_str = 'geekforgeeks best for geeks'
 
# printing original string
print("The original string is : " + str(test_str))
 
# lookup Dictionary
lookp_dict = {"best" : "good and better", "geeks" : "all CS aspirants"}
 
# performing split()
temp = test_str.split()
res = []
for wrd in temp:
     
    # searching from lookp_dict
    res.append(lookp_dict.get(wrd, wrd))
     
res = ' '.join(res)
 
# printing result 
print("Replaced Strings : " + str(res)) 
