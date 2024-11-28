"""Row-wise element Addition in Tuple Matrix
Input : test_list = [[('Gfg', 3)], [('best', 1)]] cus_eles = [1, 2] 
Output : [[('Gfg', 3, 1)], [('best', 1, 2)]] 


Input : test_list = [[('Gfg', 6), ('Gfg', 3)]] cus_eles = [7] 
Output : [[('Gfg', 6, 7), ('Gfg', 3, 7)]] """



test_list = [[('Gfg', 3), ('is', 3)], [('best', 1)], [('for', 5), ('geeks', 1)]]

print("The original list is : " + str(test_list))

cus_eles = [6, 7, 8]
res = [[sub + (cus_eles[idx], ) for sub in val] for idx, val in enumerate(test_list)]

print("The matrix after row elements addition : " + str(res))
