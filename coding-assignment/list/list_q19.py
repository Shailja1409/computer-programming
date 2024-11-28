'''to perform retention of all the records where occurrences of K is N times
Input : test_list = [(4, 5, 5, 4), (5, 4, 3)], K = 5, N = 2 
Output : [(4, 5, 5, 4)]
Input : test_list = [(4, 5, 5, 4), (5, 4, 3)], K = 5, N = 3 
Output : []   '''

test_list = [(4, 5, 6, 4, 4), (4, 4, 3), (4, 4, 4), (3, 4, 9)]
 
# printing original list
print("The original list is : " + str(test_list))
 
# initializing K
K = 4
 
# initializing N 
N = 3
 
# Retain records with N occurrences of K
# Using count() + list comprehension
res = [ele for ele in test_list if ele.count(K) == N]
 
# printing result 
print("Filtered tuples : " + str(res)) 
