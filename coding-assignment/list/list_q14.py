'''Given an array arr[] of N positive integers. The task is to find the maximum for every adjacent pair in the array.

Examples:

Input: 1 2 2 3 4 5
Output: 2 2 3 4 5

Input: 5 5
Output: 5   '''


def maximumAdjacent(arr1, n):
   
      # array to store the max 
    # value between adjacent pairs
    arr2 = []  
     
    # iterate from 1 to n - 1
    for i in range(1, n):
       
        # find max value between 
        # adjacent  pairs gets 
        # stored in r
        r = max(arr1[i], arr1[i-1])
         
        # add element 
        arr2.append(r)
         
    # printing the elements
    for ele in arr2 :
        print(ele,end=" ")
 
if __name__ == "__main__" :
   
  # size of the input array
  n = 6 
   
  # input array
  arr1 = [1,2,2,3,4,5]
   
  # function calling
  maximumAdjacent(arr1, n)
