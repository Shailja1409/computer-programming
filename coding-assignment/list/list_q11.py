'''Given a List, extract all elements whose frequency is greater than K.


Input : test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8], K = 3 
Output : [4, 3] 
Explanation : Both elements occur 4 times. 


Input : test_list = [4, 6, 4, 3, 3, 4, 3, 4, 6, 6], K = 2 
Output : [4, 3, 6] 
Explanation : Occur 4, 3, and 3 times respectively.'''

test_list = [4, 6, 4, 3, 3, 4, 3, 7, 8, 8]
 
# printing string
print("The original list : " + str(test_list))
 
# initializing K 
K = 2
 
res = [] 
for i in test_list: 
     
    # using count() to get count of elements
    freq = test_list.count(i) 
     
    # checking if not already entered in results
    if freq > K and i not in res: 
        res.append(i)
 
# printing results 
print("The required elements : " + str(res))
