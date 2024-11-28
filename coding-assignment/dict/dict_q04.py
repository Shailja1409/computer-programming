'''Given a string which contains lower alphabetic characters, we need to remove at most one character from this string in such a way that frequency of each distinct character becomes same in the string.

Examples:

Input  : str = “xyyz”
Output : Yes
We can remove character 'y' from above 
string to make the frequency of each 
character same. 

Input : str = “xyyzz” 
Output : Yes
We can remove character 'x' from above 
string to make the frequency of each 
character same.

Input : str = “xxxxyyzz” 
Output : No
It is not possible to make frequency of 
each character same just by removing at 
most one character from above string.'''

from collections import Counter 
  
def allSame(input): 
      
    # calculate frequency of each character 
    # and convert string into dictionary 
    dict=Counter(input) 
  
    # now get list of all values and push it 
    # in set 
    same = list(set(dict.values())) 
  
    if len(same)>2: 
        print('No') 
    elif len (same)==2 and same[1]-same[0]>1: 
        print('No') 
    else: 
        print('Yes') 
  
      
    # now check if frequency of all characters  
    # can become same 
      
# Driver program 
if __name__ == "__main__": 
    input = 'xxxyyzzt'
    allSame(input) 
