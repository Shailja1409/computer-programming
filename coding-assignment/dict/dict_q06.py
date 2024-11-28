'''Remove duplicate values across Dictionary Values
Input: test_dict = {'Manjeet': [1], 'Akash': [1, 8, 9]} 
Output: {'Manjeet': [], 'Akash': [8, 9]} 


Input: test_dict = {'Manjeet': [1, 1, 1], 'Akash': [1, 1, 1]} 
Output: {'Manjeet': [], 'Akash': []}'''


from collections import Counter
 
# initializing dictionary
test_dict = {'Manjeet': [1, 4, 5, 6],
             'Akash': [1, 8, 9],
             'Nikhil': [10, 22, 4],
             'Akshat': [5, 11, 22]}
 
# printing original dictionary
print("The original dictionary : " + str(test_dict))
 
# Remove duplicate values across Dictionary Values
# Using Counter() + list comprehension
cnt = Counter()
for idx in test_dict.values():
    cnt.update(idx)
res = {idx: [key for key in j if cnt[key] == 1]
       for idx, j in test_dict.items()}
 
# printing result
print("Uncommon elements records : " + str(res))
