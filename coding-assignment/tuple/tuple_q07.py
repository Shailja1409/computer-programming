'''Elements frequency in Tuple
Given a Tuple, find the frequency of each element.


Input : test_tup = (4, 5, 4, 5, 6, 6, 5) 
Output : {4: 2, 5: 3, 6: 2} 
Explanation : Frequency of 4 is 2 and so on..


Input : test_tup = (4, 5, 4, 5, 6, 6, 6) 
Output : {4: 2, 5: 2, 6: 3} 
Explanation : Frequency of 4 is 2 and so on.. '''

from collections import defaultdict
 
test_tup = (4, 5, 4, 5, 6, 6, 5, 5, 4)
 
print("The original tuple is : " + str(test_tup))
 
res = defaultdict(int)
for ele in test_tup:
     
    res[ele] += 1
 
print("Tuple elements frequency is : " + str(dict(res))) 
