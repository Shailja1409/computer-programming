'''Given dictionary list, extract dictionary with maximum keys.


Input : test_list = [{“gfg”: 2, “best” : 4}, {“gfg”: 2, “is” : 3, “best” : 4, “CS” : 9}, {“gfg”: 2}]

Output : 4

Explanation : 2nd dictionary has maximum keys, 4.


Input : test_list = [{“gfg”: 2, “best” : 4}, {“gfg”: 2}]

Output : 2

Explanation : 1st dictionary has maximum keys, 2.'''


test_list = [{"gfg": 2, "best" : 4},  
             {"gfg": 2, "is" : 3, "best" : 4},  
             {"gfg": 2}] 
  
# printing original list 
print("The original list is : " + str(test_list)) 
  
res = {}  
max_len = 0
for ele in test_list: 
      
    # checking for lengths 
    if len(ele) > max_len:  
        res = ele 
        max_len = len(ele) 
          
# printing results 
print("Maximum keys Dictionary : " + str(res)) 
