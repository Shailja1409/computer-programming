'''Given a sentence containing n words/strings. Remove all duplicates words/strings which are similar to each others.

Examples:  

Input : Geeks for Geeks
Output : Geeks for

Input : Python is great and Java is also great
Output : is also Java Python and great  '''

from collections import Counter
 
def remov_duplicates(input):
 
    # split input string separated by space
    input = input.split(" ")
 
    # now create dictionary using counter method
    # which will have strings as key and their 
    # frequencies as value
    UniqW = Counter(input)
 
    # joins two adjacent elements in iterable way
    s = " ".join(UniqW.keys())
    print (s)
 
# Driver program
if __name__ == "__main__":
    input = 'Python is great and Java is also great'
    remov_duplicates(input)
