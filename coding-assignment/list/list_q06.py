'''Given a list of lists. The task is to extract a random element from it.

Examples:

Input : test_list = [[4, 5, 5], [2, 7, 4], [8, 6, 3]]
Output : 7
Explanation : Random number extracted from Matrix.
Input : test_list = [[4, 5, 5], [2, 7, 4], [8, 6, 3]], r_no = 2
Output : 6
Explanation : Random number extracted from 2nd row from Matrix.'''

from itertools import chain
import random
 
# Initializing list
test_list = [[4, 5, 5], [2, 7, 4], [8, 6, 3]]
 
# Printing original list
print("The original list is : " + str(test_list))
 
# choice() for random number, from_iterables for flattening
res = random.choice(list(chain.from_iterable(test_list)))
 
# Printing result
print("Random number from Matrix : " + str(res))
