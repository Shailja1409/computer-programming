'''In an auction house, the prices of items are often written in a random order. The auctioneer wants the prices to be printed in increasing order to make it easier to follow.

Problem: Write a program that takes a list of prices and prints them in ascending order.

Example:

Input:
500 100 2000 1500

Output:
100 500 1500 2000 '''

def sort_prices(prices):
    price_list = list(map(int, prices.split()))
    
    price_list.sort()
    
    print(" ".join(map(str, price_list)))

input_prices = "500 100 2000 1500"
sort_prices(input_prices)
