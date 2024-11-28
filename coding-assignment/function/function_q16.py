# Given an array arr of non-negative integers, return the maximum product of two numbers possible.


def maxProduct(arr):
    a = max(arr)
    arr.pop(arr.index(a))
    b = max(arr)
    return a * b


print(maxProduct([2, 3, 4, 5, 6]))
