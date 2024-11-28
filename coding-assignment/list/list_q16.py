'''Given a list with some elements being a list of optional elements. The task is to find all the possible combinations from all options.

Examples:


Input: test_list = [1,2,3] 
Output: 
 [1], [1, 2], [1, 2, 3], [1, 3]
 [2], [2, 3], [3]    '''


from itertools import combinations
# initializing list
test_list = ["GFG", [5, 4], "is",
            ["best", "good", "better", "average"]]
idx=0
temp = combinations(test_list, 2)
for i in list(temp):
    idx = idx+1
    print ("Combination", idx, ": ", i)
