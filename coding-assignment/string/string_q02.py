'''The town market is having a sale, and the shopkeeper wants to display the price tags in reverse order for some reason. The prices of the items are written in a single line, and you are tasked with reversing the digits of each price individually.

Problem: Write a Python program that reads a list of prices, reverses the digits of each price, and prints the reversed prices.

Example:

Input:
123 456 789

Output:
321 654 987'''

def reverse_prices(prices):
    
    prices_list = prices.split()
    
    reversed_prices = [price[::-1] for price in prices_list]
    
    print(" ".join(reversed_prices))

input_prices = "123 456 789"
reverse_prices(input_prices)
