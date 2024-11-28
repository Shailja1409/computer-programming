'''Assign Frequency to Tuples
Given tuple list, assign frequency to each tuple in list.


Input : test_list = [(6, 5, 8), (2, 7), (6, 5, 8), (9, ), (2, 7)] 
Output : [(6, 5, 8, 2), (2, 7, 2), (9, 1)] 
Explanation : (2, 7) occurs 2 times, hence 2 is append in tuple.
Input : test_list = [(2, 7), (2, 7), (6, 5, 8), (9, ), (2, 7)] 
Output : [(6, 5, 8, 1), (2, 7, 3), (9, 1)] 
Explanation : (2, 7) occurs 3 times, hence 3 is append in tuple. '''

from collections import Counter
 
# initializing list
test_list = [(6, 5, 8), (2, 7), (6, 5, 8), (6, 5, 8), (9, ), (2, 7)]
 
# printing original list
print("The original list is : " + str(test_list))
 
# one-liner to solve problem
# assign Frequency as last element of tuple
res = [(*key, val) for key, val in Counter(test_list).items()]
 
# printing results
print("Frequency Tuple list : " + str(res))
