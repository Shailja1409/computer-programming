'''Remove Tuples of Length K
Input : test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)], K = 2 
Output : [(4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)] 
Explanation : (4, 5) of len = 2 is removed. 


Input : test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)], K = 3 
Output : [(4, 5), (4, ), (1, ), (3, 4, 6, 7)] 
Explanation : 3 length tuple is removed.  '''


test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
 
print("The original list : " + str(test_list))
 
K = 1
 
res = [ele for ele in test_list if len(ele) != K]
  
print("Filtered list : " + str(res))
